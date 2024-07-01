from django.contrib import admin
from common.models import Page,GalleryPhoto,Settings,TimeStepModel
from modeltranslation.admin import TranslationAdmin

# Register your models here.

admin.site.register(GalleryPhoto)
admin.site.register(Settings)
# admin.site.register(TimeStepModel)






class PageAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}
    group_fieldsets = True

admin.site.register(Page,PageAdmin)








