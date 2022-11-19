from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from api.models import product


# nested serializers
class sampleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ["id","title","price"]


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","username","first_name","last_name"]








# detaile sabade kharid
class cartItemSerializer(serializers.ModelSerializer):
    sub_total = serializers.SerializerMethodField(method_name="total_price")
    order = serializers.StringRelatedField()
    product = sampleProductSerializer(many=False)
    class Meta:
        model = models.cartItem
        fields = ["id","order","product","quantity","sub_total"]

    def total_price(self , item:models.cartItem):
        return int(item.product.price * item.quantity)


class cartSerializer(serializers.ModelSerializer):
    items = cartItemSerializer(many=True) # chon daronesh cartItem haye ziadi hast bayad many=True bashe
    grand_total = serializers.SerializerMethodField(method_name="total_payment")
    # inja product haye ziadi gharare neshon dade she
    user = userSerializer()
    class Meta:
        model = models.cart
        fields = ["user","is_paid","payment_date","items","grand_total"]





    def total_payment(self, cart:models.cart):
        items = cart.items.all() # hame product hayi ke hast ro miare
        total = sum([item.quantity * item.product.price for item in items ])
        return total



