from order.landing import serializers
from order.models import Order
from rest_framework import generics

class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderListSerializer
    
