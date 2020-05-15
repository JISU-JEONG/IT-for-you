from rest_framework import serializers
from .models import *
class ProblemBasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProblemBasic
    fields = '__all__'

class AnswerBasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProblemBasic
    fields = '__all__'

class ProblemAndAnswerSerializer(ProblemBasicSerializer):
  answers = AnswerBasicSerializer(source='answerbasic_set', many=True)
  class Meta(ProblemBasicSerializer.Meta):
    fields = ProblemBasicSerializer.Meta.fields