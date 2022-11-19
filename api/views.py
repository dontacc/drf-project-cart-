from . import models
from . import serializers

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView






# class productViewSet(ModelViewSet):
#     queryset = models.product.objects.all()
#     serializer_class = serializers.productSerializers


class productView(ListCreateAPIView):
    queryset = models.product.objects.all()
    serializer_class = serializers.productSerializers



class addCartView(APIView):
    serializer_classes = serializers.productSerializers

    def post(self,request):
        serializer = serializers.cartSerializers
        if serializer.is_valid():
            order_item = serializer.validated_data.get("order_item")
            serializer.save()
            return Response({"message":"ordered added successfully in your cart"},status=201)
        else:
            return Response(serializer.errors)









# class addCartView(APIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_classes = serializers.cartSerializers
#
#     def post(self,request):
#         serializer = serializers.cartSerializers(data=request.data)
#         if serializer.is_valid():
#             cart = serializer.validated_data.get("title")
#             serializer.save()
#             return Response({"message":"your product added to the cart!"},status=200)
#         else:
#             return Response(serializer.errors("somthing is wrong try again" , status=404))






# submitting data
# class productView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = serializers.productSerializers
#
#     def post(self, request):
#         serializer = serializers.productSerializers(data=request.data)
#         if serializer.is_valid():
#             title = serializer.validated_data.get("title")
#             price = serializer.validated_data.get("price")
#             serializer.save()
#             return Response({"message ": "the product created successfully!"}, status=201)
#         else:
#             # return Response("The creation failed" , status=status.HTTP_400_BAD_REQUEST)
#             return Response(serializer.errors)
#
