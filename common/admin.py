from django.contrib import admin
from common.models import Page,GalleryPhoto,Settings,TimeStepModel
from modeltranslation.admin import TranslationAdmin
# Register your models here.

admin.site.register(GalleryPhoto)
admin.site.register(Settings)
# admin.site.register(TimeStepModel)

@admin.register(Page)
class PageAdminTranslation(TranslationAdmin):
    list_display = ('title',)
    group_fieldsets = True



