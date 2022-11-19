import logging

from azbankgateways import bankfactories
from azbankgateways.exceptions import AZBankGatewaysException
from cart import models
from rest_framework.views import APIView


# action by default methode get ro mifreste age methodesho malom nakonim
class paymentGateaway(APIView):
    def get(self, request):
        # خواندن مبلغ از هر جایی که مد نظر است
        ListCart = models.cartItem.objects.all()
        amount = sum([item.quantity * item.product.price for item in ListCart])
        # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
        user_mobile_number = '+989112221234'  # اختیاری

        factory = bankfactories.BankFactory()
        try:
            # az create zamani estefade mikonim ke mikhaym be on banke maghsad mostaghim vasl shim va banke
            # dg nadarim, autocreate ag bezanim mire kole gateway haro miagarde toshon ag  banki faild shod
            bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
            bank.set_request(request)
            bank.set_amount(amount)
            # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
            # bank.set_client_callback_url(reverse('callback-gateway'))
            bank.set_client_callback_url('/callback-gateway/')
            bank.set_mobile_number(user_mobile_number)  # اختیاری

            # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
            # پرداخت برقرار کنید.
            bank_record = bank.ready()

            # هدایت کاربر به درگاه بانک
            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            # TODO: redirect to failed page.
            raise e
