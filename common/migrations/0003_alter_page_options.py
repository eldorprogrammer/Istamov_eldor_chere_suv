# Generated by Django 5.0.6 on 2024-06-27 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_page_content_ru_page_content_uz_page_title_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Postlar'},
        ),
    ]