from django.shortcuts import render
from common.landing import serializers
from rest_framework.generics import ListAPIView,GenericAPIView,RetrieveAPIView
from rest_framework.response import Response
from common import models
import random
# Create your views here.


class SettingsAPIVew(GenericAPIView):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingsSerializers


    def get(self, request, *args, **kwargs, ):
        settings = models.Settings.objects.all().first()
        serializer = self.get_serializer(settings)

        return Response(serializer.data)
    

class GaleryPhotoRandomAPIView(ListAPIView):
    serializer_class = serializers.GaleryGetSerializer

    def get_queryset(self):
        queryset = list(models.GalleryPhoto.objects.all())
        random.shuffle(queryset)

        return queryset
    

class PageAPIView(RetrieveAPIView):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    lookup_field = 'slug'
