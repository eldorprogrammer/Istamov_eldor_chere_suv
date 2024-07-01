from django.db import models

from django.contrib.auth.models import AbstractUser,Group,Permission
from common.models import TimeStepModel

# Create your models here.


class User(AbstractUser):
    telegram_id = models.BigIntegerField('telegram id',unique = True,blank=True,null=True)
    full_name = models.CharField("full name", max_length=200)
    phone = models.CharField('phone number',max_length=15)
    email = models.EmailField('email',unique = True)
    lang = models.CharField(max_length = 20, choices = [("uz","O'zbek"), ("ru","Russian")], default = 'uz')

    def __str__(self) -> str:
        return self.email
    first_name = None
    last_name = None
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

# User contact jadvali

class UserContactAplication(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField('email')
    phone = models.CharField('phone nummber',max_length=15)

    def __str__(self) -> str:
        return self.phone