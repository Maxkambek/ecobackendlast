from modeltranslation.translator import TranslationOptions, register
from .models import Functions, DetailFunctions, AnswerQuestions, Xizmatlar, Maqola


@register(Functions)
class FuncTrans(TranslationOptions):
    fields = ['name']


@register(DetailFunctions)
class DetailTrans(TranslationOptions):
    fields = ['title', 'content', 'sub_title', 'sub_content']


@register(Maqola)
class MaqolaTrans(TranslationOptions):
    fields = ['title', 'content']


@register(AnswerQuestions)
class AnswerTrans(TranslationOptions):
    fields = ['question', 'answer']


@register(Xizmatlar)
class XizmatTrans(TranslationOptions):
    fields = ['text']
