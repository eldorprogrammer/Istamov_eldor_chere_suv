from common.models import Page

from modeltranslation.translator import TranslationOptions,register

@register(Page)
class PageTranslation(TranslationOptions):
    fields = ('title','content')




