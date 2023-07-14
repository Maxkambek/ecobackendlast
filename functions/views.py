from rest_framework import generics
from .serializers import FunctionsSerializer, AnswerSerializer, XizmatlarSerializer, MaqolaSerializer
from .models import Functions, AnswerQuestions, Xizmatlar, Maqola


class FunctionAPIView(generics.ListAPIView):
    queryset = Functions.objects.all()
    serializer_class = FunctionsSerializer


class AnswerAPIView(generics.ListAPIView):
    queryset = AnswerQuestions.objects.all()
    serializer_class = AnswerSerializer


class XizmatlarAPIView(generics.ListAPIView):
    queryset = Xizmatlar.objects.all()
    serializer_class = XizmatlarSerializer


class MaqolaAPIView(generics.ListAPIView):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
