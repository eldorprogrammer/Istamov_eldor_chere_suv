from rest_framework import serializers
from common import models


class SettingsGetEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Settings
        fields = '__all__'