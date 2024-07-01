from rest_framework import serializers
from common import models


class SettingsGetEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Settings
        fields = '__all__'


class GaleryPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GalleryPhoto
        fields = '__all__'


# class SlugSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = models.Page
#         fields = ['slug', 'title', 'content']
        
