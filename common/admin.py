from django.contrib import admin
from django.http import HttpRequest
from common.models import Page,GalleryPhoto,Settings,TimeStepModel
from modeltranslation.admin import TranslationAdmin

# Register your models here.

admin.site.register(GalleryPhoto)

# admin.site.register(TimeStepModel)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Settings.objects.exists():
            return False
        return True
    
    def has_delete_permission(self, request,  obj=None ):
        return False





class PageAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}
    group_fieldsets = True

admin.site.register(Page,PageAdmin)








