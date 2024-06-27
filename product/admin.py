from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Product
# Register your models here.


@admin.register(Product)
class ProductAdminTranslation(TranslationAdmin):

    list_display = ('name',)
    group_fieldsets = True

    