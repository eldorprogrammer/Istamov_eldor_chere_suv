from django.contrib import admin
from common.models import Page
from modeltranslation.admin import TranslationAdmin
# Register your models here.


@admin.register(Page)
class PageAdminTranslation(TranslationAdmin):
    list_display = ('title',)
    group_fieldsets = True



