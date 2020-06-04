from rest_framework import serializers
from .models import *
from IPython import embed
from myprobs.models import *

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
    fields = ('p_id', 'p_question', 'p_commentary', 'p_code', 'pc_id', 'pt_id', 'pd_id')

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = ('a_id', 'p_id', 'a_value', 'a_correct')

class ProblemDetailSerializer(ProblemSerializer):
  category = ProbCateSerializer(source='pc_id')
  answers = serializers.SerializerMethodField()
  myprob_check = serializers.SerializerMethodField()
  
  class Meta(ProblemSerializer.Meta):
    fields = ProblemSerializer.Meta.fields + ('answers', 'category', 'myprob_check',)
  
  def get_answers(self, obj):
    answers = obj.answer_set.all().order_by('?')
    return AnswerSerializer(answers, many=True).data

  def get_myprob_check(self, obj):
    user_id = self.context.get('user_id')
    myprob = MyProb.objects.filter(user=user_id, prob=obj.p_id)
    if myprob:
      return True
    else:
      return False


class ProbPostSerializer(serializers.ModelSerializer):
  TestHere = serializers.CharField()
  class Meta:
    model = Problem
    fields = ('TestHere',)