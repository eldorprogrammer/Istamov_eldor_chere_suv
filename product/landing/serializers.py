from rest_framework import serializers
from product import models

   


class ProducGetSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Product.objects.all()
        fields = [
                'name',
                'content',
                'price',
                'order'
        ]