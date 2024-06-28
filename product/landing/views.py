from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from product.landing import serializers
from product import models

class ProductGetAPIView(GenericAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProducGetSerializer


    def get(self, request, *args, **kwargs):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data)
    
    