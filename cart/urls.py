from django.urls import path

from .view import cartitemView, cartView, detailitemView

urlpatterns = [
    path("situation", cartView.CartView.as_view(), name="cart-page"),  # carts
    path("", cartitemView.CartItemView.as_view(), name="cartItem-page"),  # itemCarts
    path("<int:pk>/", detailitemView.DetailItemView.as_view(), name="delete-item"),  # for delete the object

]
