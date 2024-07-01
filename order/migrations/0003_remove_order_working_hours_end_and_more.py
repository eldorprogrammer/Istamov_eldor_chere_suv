# Generated by Django 4.2.3 on 2024-06-30 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='working_hours_end',
        ),
        migrations.RemoveField(
            model_name='order',
            name='working_hours_start',
        ),
        migrations.AddField(
            model_name='order',
            name='created_add',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_add',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]