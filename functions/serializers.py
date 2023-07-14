from rest_framework import serializers
from .models import Functions, DetailFunctions, AnswerQuestions, Xizmatlar, Maqola


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailFunctions
        fields = ['id', 'image', 'title', 'content', 'sub_image', 'sub_title', 'sub_content']


class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = ['id', 'image', 'title', 'content']
        

class FunctionsSerializer(serializers.ModelSerializer):
    detail_func = DetailSerializer(many=True)

    class Meta:
        model = Functions
        fields = ['id', 'image', 'name', 'detail_func']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestions
        fields = ['id', 'question', 'answer']


class XizmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmatlar
        fields = ['id', 'text']
