from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from api.models import product


# sabade kharid
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)  # karbari ke sabade kharid barash baz mishe hamon lahze ke
    # pardakht nemikone baraye hamin null va blank mitone bashe ta ye timi


    def __str__(self):
        return self.user.username




class cartItem(models.Model):
    order = models.ForeignKey(cart, on_delete=models.CASCADE, related_name="items", null=True, blank=True)
    #  in items other ro mitonim dar field haye on yeki class dar serializer estefade konim
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True, related_name="cartitems")
    quantity = models.IntegerField(verbose_name="تعداد")

    def __str__(self):
        return self.product.title





    # dalile inke true hast nullesh ine ke momkene badan bekhaym pardakht konim va bayad khali bemone felan
    # dar digikala ta hazinaro pardakht nakardim final_price khali mimone va gheymate mahsol az dakhele product
    # mohasebe mishe
