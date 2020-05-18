from rest_framework import serializers
from .models import *
class ProblemBasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProblemBasic
    fields = ('p_id', 'p_category', 'p_question', 'p_type', 'p_diff', 'p_code')

class AnswerBasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = AnswerBasic
    fields = ('a_id', 'p_id', 'a_value', 'a_correct',)

class ProblemAndAnswerSerializer(ProblemBasicSerializer):
  answers = AnswerBasicSerializer(source='answerbasic_set', many=True)
  class Meta(ProblemBasicSerializer.Meta):
    fields = ProblemBasicSerializer.Meta.fields + ('answers',)