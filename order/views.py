from django.shortcuts import render
from rest_framework import serializers,generics
from order import serializers,models
from rest_framework.permissions import IsAdminUser
# Create your views here.

class OrderListAPIView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListRetrieveSerializer
    permission_classes = [IsAdminUser, ]


class OrderRetrieveAPIView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListRetrieveSerializer
    permission_classes = [IsAdminUser, ]


class OrderEditAPIView(generics.DestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderEditSerializer
    permission_classes = [IsAdminUser, ]





