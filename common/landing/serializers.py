from rest_framework.serializers import ModelSerializer
from common import models




class SettingsSerializers(ModelSerializer):

    class Meta:
        model = models.Settings
        fields = [

                  'contact_telegram',
                  'contact_phone',
                  'longitude',
                  'latitute',
                  'location_text',
                  'working_hours_start',
                  'working_hours_end',
                  'telegram_bot'

        ]


class GaleryGetSerializer(ModelSerializer):
    class Meta:
        model = models.GalleryPhoto
        fields = ['image']


class PageSerializer(ModelSerializer):

    class Meta:

        model = models.Page
        fields = ['slug', 'title', 'content']
        read_only_fields = ['slug']
        
        




    