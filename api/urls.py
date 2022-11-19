from django.urls import path
from . import views
from rest_framework import routers



# app_name = "api"
# router = routers.SimpleRouter()
# router.register("products" , views.productViewSet.as_view() , basename="product")
# urlpatterns = router.urls

urlpatterns = [
    path("products/" ,views.productView.as_view() , name="product_list"),
]

# urlpatterns = [
#     path("products/", views.productView.as_view(), name="product_view"),
#     path("products/<slug:slug>", views.detialView.as_view(), name="detail_page"),
#     path("add_cart/" , views.addCartView.as_view() , name="cart_page")
#     # path("add_cart_view/" , views.addCartView.as_view()),
#     # path("cart/" , views.showOrders.as_view() , name="cart-page")
# ]
