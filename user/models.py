from django.db import models

from django.contrib.auth.models import AbstractUser,UserManager,Group,Permission
from common.models import TimeStepModel
from django.contrib.auth.hashers import make_password

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user( email, password, **extra_fields)



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
    objects = CustomUserManager()
    

# User contact jadvali

class UserContactAplication(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField('email')
    phone = models.CharField('phone nummber',max_length=15)
    is_contacted = models.BooleanField()


    def __str__(self) -> str:
        return self.phone
    
