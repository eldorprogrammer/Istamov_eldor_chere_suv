from order import models
from rest_framework.serializers import ModelSerializer



class OrderListSerializer(ModelSerializer):
    class Meta:

        model = models.Order
        fields = [
            'id',
            'product',
            'customer',
            'count',
            'free_count',
            'longitude',
            'latetude',
            'product_price',
            'total_price'
            ]

