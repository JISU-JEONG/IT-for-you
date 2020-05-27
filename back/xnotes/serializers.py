from rest_framework import serializers
from .models import *
from problems.serializers import *
from IPython import embed

class XnoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xnote
        fields = ('id', 'user', 'prob', 'u_answer')

class MyNoteListSerializer(XnoteSerializer):

    pc_value = serializers.SerializerMethodField()
    p_question = serializers.SerializerMethodField()
    p_code = serializers.SerializerMethodField()
    class Meta(XnoteSerializer.Meta):
        fields = ('id', 'pc_value', 'p_question', 'p_code')

    def get_pc_value(self, obj):
        return obj.prob.pc_id.pc_value

    def get_p_question(self, obj):
        return obj.prob.p_question
    
    def get_p_code(self, obj):
        return obj.prob.p_code
