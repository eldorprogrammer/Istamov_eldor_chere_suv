from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# from django.utils.translation import gettext_lazy as _
# Create your models here.


class Product(models.Model):
    name = models.CharField('name',max_length=200)
    content = RichTextUploadingField(verbose_name = ('content'))
    price = models.BigIntegerField('narxi')
    order = models.IntegerField('buyurtma')


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'mahsulot'
        verbose_name_plural = 'mahsulotlar'



class FreeProduct(models.Model):
    free_count = models.OneToOneField(Product,on_delete=models.CASCADE)
    product = models.BigIntegerField('product')
    count = models.BigIntegerField('count')

    def __str__(self) -> str:
        return str(self.product)
    

  