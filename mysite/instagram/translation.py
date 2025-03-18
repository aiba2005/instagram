from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Post)
class NetworkTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Comment)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('text',)



