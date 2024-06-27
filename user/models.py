from django.db import models

from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.


class User(AbstractUser):
    telegram_id = models.BigIntegerField('telegram id',null=True)
    full_name = models.CharField("full name", max_length=200)
    phone = models.CharField('phone number',max_length=15)
    email = models.EmailField('email')
    password = models.CharField('password',max_length=50)
    is_admin = models.BooleanField('admin',default=False)



    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self) -> str:
        return self.full_name
    

# User contact jadvali

class UserContactAplication(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField('email')
    phone = models.CharField('phone nummber',max_length=15)

    def __str__(self) -> str:
        return self.phone