# Generated by Django 5.0.6 on 2024-06-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_uz',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
    ]
