from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math
from django.db.models import F, Sum


class product(models.Model):
    title = models.CharField(max_length=225, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")

    def __str__(self):
        return self.title


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_time = models.DateTimeField(default=timezone.now)
#     order_item = models.ManyToManyField(product)
#     quantity = models.PositiveIntegerField(default=1)
#     total_price = models.IntegerField(default=0)

    # @property
    # def total_price(self):
    #     total_price = (self.quantity * product.price)
    #     return total_price

    # @classmethod
    # def __mul__(self):
    #     return (self.quantity * product.price)
    #
    # def save(self, *args, **kwargs):
    #     self.total_price = self.__mul__()
    #     super().save(*args, **kwargs)
