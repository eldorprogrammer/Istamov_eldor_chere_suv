from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Product,FreeProduct
# Register your models here.

admin.site.register(FreeProduct)

@admin.register(Product)
class ProductAdminTranslation(TranslationAdmin):

    list_display = ('name',)
    group_fieldsets = True
    # readonly_fields = ['created_add','updated_add']

    