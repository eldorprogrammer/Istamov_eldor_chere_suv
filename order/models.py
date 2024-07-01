from django.db import models
from product.models import Product
from user.models import User
from common.models import TimeStepModel
# Create your models here.


GEEKS_CHOICES =( 
    ("tayyorlanmoqda", "tayyorlanmoqda"), 
    ("yo'lda", "yo'lda"), 
    ("yetib keldi", "yetib keldi"), 
    ("yetkaziy yakunlandi", "yatkazish yakunlandi"), 
   
)



class Order(TimeStepModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orders')
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    count = models.IntegerField('soni')
    free_count = models.BigIntegerField('tekinlari soni',default=0)
    longitude = models.FloatField('uzunlik')
    latetude = models.FloatField('kenglik')
    status = models.CharField('status',choices=GEEKS_CHOICES,max_length=250)
    product_price = models.BigIntegerField('product price')
    total_price = models.BigIntegerField('total price')
    status_changed_ad = models.BigIntegerField('statusga ozgarish qoshish')

    def __str__(self) -> str:
        return str(self.count)
