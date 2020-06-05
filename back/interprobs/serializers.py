from rest_framework import serializers
from .models import Interview
from problems.models import *
from problems.serializers import *
from django.shortcuts import get_object_or_404
import base64
class InterviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'

class ProbInfoForInterview(serializers.ModelSerializer):
    category = ProbCateSerializer(source='pc_id')
    class Meta:
        model = Problem
        fields = ('p_id', 'p_code', 'p_question', 'category',)


class MyInterListSerializers(InterviewSerializers):
    category = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()
    p_question = serializers.SerializerMethodField()
    class Meta(InterviewSerializers.Meta):
        fields = ('id', 'category', 'company', 'p_question',)

    def get_category(self, obj):
        return obj.prob.pc_id.pc_value

    def get_company(self, obj):
        return obj.prob.p_code

    def get_p_question(self, obj):
        return obj.prob.p_question


class MyInterDetailSerializers(MyInterListSerializers):
    p_answer = serializers.SerializerMethodField()
    myanswer = serializers.SerializerMethodField()
    audio_data = serializers.SerializerMethodField()
    class Meta(MyInterListSerializers.Meta):
        fields = ('id', 'category', 'company', 'p_question', 'p_answer', 'myanswer', 'audio_data')

    def get_p_answer(self, obj):
        return obj.prob.p_commentary

    def get_myanswer(self, obj):
        return obj.content
    
    def get_audio_data(self, obj):
        audio_data = obj.file.read()
        audio_data = 'data:audio/mpeg;base64,' + base64.b64encode(audio_data).decode('utf-8')
        return audio_data