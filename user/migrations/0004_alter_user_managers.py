# Generated by Django 4.2.3 on 2024-07-01 06:20

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_first_name_remove_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.models.CustomUserManager()),
            ],
        ),
    ]