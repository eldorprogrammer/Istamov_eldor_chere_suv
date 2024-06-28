from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os
from datetime import datetime

# Create your models here.

def upload_to(instance, filename):
    # Get the current date
    today = datetime.today()
    # Format the date-based path
    path = today.strftime('uploads/%Y/%m/%d')
    # Construct the full upload path
    return os.path.join(path, filename)


class GalleryPhoto(models.Model):
    image = models.ImageField('image',upload_to=upload_to)

    # def __str__(self) -> str:
    #     return str(self.image)


    class Meta:
        verbose_name_plural = 'Galery/'

        


class Page(models.Model):
    slug = models.SlugField('slug',default="",null=False)
    title = models.CharField('title',max_length=250,)
    content = RichTextUploadingField()


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'





class TimeStepModel(models.Model):
    working_hours_start = models.CharField('ish boshlanish vaqti',max_length=10)
    working_hours_end = models.CharField('ish tugash vaqti',max_length=10)

    class Meta:
        abstract = True



class Settings(TimeStepModel):
    contact_telegram = models.CharField('contact telegram',max_length=100,default=0)
    contact_phone = models.CharField('contact phone',max_length=15)
    longitude = models.FloatField("uzunlik")
    latitute = models.FloatField('kenglik')
    location_text = models.TextField('location text')
    telegram_bot = models.CharField('telegram bot',max_length=100)


    def __str__(self) -> str:
        return self.contact_telegram
    





