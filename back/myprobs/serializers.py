from rest_framework import serializers
from .models import *
from problems.serializers import *

class MyProbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProb
        fields = ('id', 'user', 'prob',)

class MyProbListSerializer(MyProbSerializer):
    problems = ProblemSerializer(source='prob')
    class Meta(MyProbSerializer.Meta):
        fields = MyProbSerializer.Meta.fields + ('problems',)

class MyProbDetailSerializer(MyProbSerializer):
    problems = ProblemSerializer(source='prob')
    answers = AnswerSerializer(source='prob.answer_set', many=True)
    class Meta(MyProbSerializer.Meta):
        fields = MyProbSerializer.Meta.fields + ('problems', 'answers',)