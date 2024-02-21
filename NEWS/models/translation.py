from modeltranslation.translator import register, TranslationOptions, translator
from .models import News, Category

@register(News)
class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Category)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('name',)