from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
import os
from datetime import datetime

# Create your models here.


class TimeStepModel(models.Model):
    created_at = models.TimeField( blank = True, null=True)
    updated_at = models.TimeField( blank = True, null = True)

    class Meta:
        abstract = True



def upload_to(instance, filename):
    # Get the current date
    today = datetime.today()
    # Format the date-based path
    path = today.strftime('uploads/%Y/%m/%d')
    # Construct the full upload path
    return os.path.join(path, filename)


class GalleryPhoto(TimeStepModel):
    image = models.ImageField('image',upload_to='uploads/%Y/%m/%d')


    class Meta:
        verbose_name_plural = 'Galery/'

    



class Page(TimeStepModel):
    title = models.CharField('title',max_length=250,)
    slug = models.SlugField('slug',default="",null=False)
    content = RichTextUploadingField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'









class Settings(TimeStepModel):
    contact_telegram = models.CharField('contact telegram',max_length=100,default=0)
    contact_phone = models.CharField('contact phone',max_length=15)
    longitude = models.FloatField("uzunlik")
    latitute = models.FloatField('kenglik')
    location_text = models.TextField('location text')
    telegram_bot = models.CharField('telegram bot',max_length=100)


    def __str__(self) -> str:
        return self.contact_telegram
    





