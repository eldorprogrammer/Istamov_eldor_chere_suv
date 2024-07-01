from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from product import serializers,models
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# Create your views here.

class ProductListAPIView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAdminUser]


class ProductCreateAPIView(CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAdminUser, ]

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAdminUser, ]


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAdminUser, ]


class ProductDestroyAPIView(RetrieveDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAdminUser, ]



