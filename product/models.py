from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from common.models import TimeStepModel
# Create your models here.


class Product(TimeStepModel):
    
    name = models.CharField('name',max_length=200)
    content = RichTextUploadingField(verbose_name=_('content'))
    price = models.BigIntegerField('narxi')
    order = models.IntegerField('buyurtma')
    is_active = models.BooleanField('activligi',null=True,blank=True)


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = _('mahsulot')
        verbose_name_plural =_('mahsulotlar')



class FreeProduct(TimeStepModel):
    free_count = models.OneToOneField(Product,on_delete=models.CASCADE)
    product = models.BigIntegerField('product')
    count = models.BigIntegerField('count')

    def __str__(self) -> str:
        return str(self.product)
    

  