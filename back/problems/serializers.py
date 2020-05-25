from rest_framework import serializers
from .models import *

class ProbCateSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProbCate
    fields = ('pc_id', 'pc_value',)

class ProbTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProbType
    fields = ('pt_id', 'pt_value')

class ProbDiffSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProbDiff
    fields = ('pd_id', 'pd_value')

class ProblemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Problem
    fields = ('p_id', 'p_question', 'p_code', 'pc_id', 'pt_id', 'pd_id')

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = ('a_id', 'p_id', 'a_value', 'a_correct')

class ProblemDetailSerializer(ProblemSerializer):
  category = ProbCateSerializer(source='pc_id')
  answers = AnswerSerializer(source='answer_set', many=True)
  
  class Meta(ProblemSerializer.Meta):
    fields = ProblemSerializer.Meta.fields + ('answers', 'category',)

class ProbPostSerializer(serializers.ModelSerializer):
  test = serializers.ListField()
  class Meta(ProblemSerializer.Meta):
    fields = ('test',)