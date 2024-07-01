from django.shortcuts import render
from common import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from common import models
# Create your views here.


class SettingsGetEditAPIView(generics.GenericAPIView):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingsGetEditSerializer
    permission_classes = [IsAdminUser,]


    def get(self, request, *args, **kwargs):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(*args, setting, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)


class GaleryPhotoListAPIView(generics.ListAPIView):
    queryset = models.GalleryPhoto.objects.all()
    serializer_class = serializers.GaleryPhotoSerializer
    permission_classes = [IsAdminUser, ]


class GaleryPhotoCreateAPIView(generics.CreateAPIView):
    queryset = models.GalleryPhoto.objects.all()
    serializer_class = serializers.GaleryPhotoSerializer
    permission_classes = [IsAdminUser, ]


class GaleryPhotoRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.GalleryPhoto.objects.all()
    serializer_class = serializers.GaleryPhotoSerializer
    permission_classes = [IsAdminUser, ]


