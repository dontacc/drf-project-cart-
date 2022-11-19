from rest_framework.views import APIView
from cart import models
from cart import serializers
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404


class DetailItemView(APIView):
    # def get(self,request,pk):
    #     detail = get_object_or_404(models.cartItem,pk=pk)
    #     serializer = serializers.cartItemSerializer(detail,many=False)
    #     return Response(serializer.data)

    def delete(self, request, pk):
        detail = get_object_or_404(models.cartItem, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
