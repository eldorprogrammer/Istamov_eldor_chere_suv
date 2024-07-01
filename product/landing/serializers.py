from rest_framework import serializers
from product import models

   


class ProducGetSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Product
        fields = [
                'name',
                'content',
                'price',
                'order'
        ]