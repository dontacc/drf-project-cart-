import logging

from azbankgateways import models as bank_models, default_settings as settings
from django.http import HttpResponse, Http404
from rest_framework.views import APIView


class callbackView(APIView):
    def get(self, request):
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            logging.debug("این لینک معتبر نیست.")
            raise Http404
        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

        # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
        if bank_record.is_success:
            # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
            # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
            return HttpResponse("پرداخت با موفقیت انجام شد.")

        # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
        return HttpResponse(
            "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")
