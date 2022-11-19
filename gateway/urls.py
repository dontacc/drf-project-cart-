from django.urls import path

from .view import callback, gateway

urlpatterns = [
    path("go-to-gateway/", gateway.paymentGateaway.as_view(), name="gateway-page"),
    path("callback-gateway/", callback.callbackView.as_view(), name="callback-page"),
]


