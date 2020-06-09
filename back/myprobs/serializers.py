from rest_framework import serializers
from .models import *
from problems.serializers import *

class MyProbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProb
        fields = ('id', 'user', 'prob',)

class MyProbListSerializer(MyProbSerializer):
    problems = ProblemSerializer(source='prob')
    answers = AnswerSerializer(source='prob.answer_set', many=True)
    answer_list = serializers.SerializerMethodField()
    class Meta(MyProbSerializer.Meta):
        fields = MyProbSerializer.Meta.fields + ('problems', 'answers', 'answer_list')

    def get_answer_list(self, obj):
        answers = obj.prob.answer_set.all()
        answer_list = []
        for ans in answers:
            if ans.a_correct:
                answer_list.append(ans.a_value)
        return answer_list

class MyProbDetailSerializer(MyProbSerializer):
    problems = ProblemSerializer(source='prob')
    answers = AnswerSerializer(source='prob.answer_set', many=True)
    class Meta(MyProbSerializer.Meta):
        fields = MyProbSerializer.Meta.fields + ('problems', 'answers',)

    