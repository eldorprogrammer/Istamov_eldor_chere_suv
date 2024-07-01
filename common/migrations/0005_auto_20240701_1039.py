# Generated by Django 4.2.3 on 2024-07-01 05:39

from django.db import migrations

from common.models import Settings

def create_settings(*args, **kwargs):
    Settings.objects.create(
        created_at = "08:00:00",
        updated_at = "23:59:00",
        contact_telegram = "chereuz",
        contact_phone = '+933333333',
        longitude = 22.3,
        latitute = 1.2,
        location_text = 'text',
        telegram_bot = 'chereuzbot'


    )

class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_galleryphoto_created_at_and_more'),
    ]
    atomic = False
    operations = [
        migrations.RunPython(create_settings)
    ]