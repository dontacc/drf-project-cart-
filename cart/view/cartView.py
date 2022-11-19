from cart import models
from cart import serializers
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


class CartView(APIView):
    def get(self, request):
        listSituation = models.cart.objects.all()
        serializer = serializers.cartSerializer(listSituation, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.cartSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            is_paid = serializer.validated_data.get("is_paid")
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


