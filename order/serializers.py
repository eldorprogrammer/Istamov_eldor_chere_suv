from rest_framework import serializers
from order.models import Order

class OrderListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['status',]

        

        
