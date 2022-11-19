"""drf_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from azbankgateways.urls import az_bank_gateways_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("restframework-auth", include('rest_framework.urls')),
    path("api/", include("api.urls")),

    # path("api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),


    path("carts/" , include("cart.urls")),
    # path("account/" , include("account.urls"))


    # payment gateways:
    # bara inke package betone vasl beshe be dargahe bank va response dargahe bank
    path("bankgateways/" , az_bank_gateways_urls()),
    path("" , include("gateway.urls")),



]
