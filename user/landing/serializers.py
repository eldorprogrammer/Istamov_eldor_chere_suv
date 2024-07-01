
from user import models
from rest_framework import serializers


class UserAplicationSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserContactAplication
        fields = []