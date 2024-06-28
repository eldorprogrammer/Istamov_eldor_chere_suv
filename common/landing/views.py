from django.shortcuts import render
from common.landing import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from common import models
# Create your views here.


class SettingsAPIVew(GenericAPIView):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingsSerializers


    def get(self, request, *args, **kwargs, ):
        settings = models.Settings.objects.all().first()
        serializer = self.get_serializer(settings)

        return Response(serializer.data)
    

# class GaleryGetView(GenericAPIView):
#     queryset = models.GalleryPhoto.objects.all()
#     serializer_class = serializers.GaleryGetSerializer

#     def get()
