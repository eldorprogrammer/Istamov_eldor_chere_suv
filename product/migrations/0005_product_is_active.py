# Generated by Django 5.0.6 on 2024-06-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_content_alter_product_content_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(blank=True, null=True, verbose_name='activligi'),
        ),
    ]
