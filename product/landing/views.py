from rest_framework.generics import ListAPIView
from product.landing import serializers
from product import models

class ProductGetAPIView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProducGetSerializer



    
    
    