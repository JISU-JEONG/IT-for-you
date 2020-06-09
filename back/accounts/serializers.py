from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
from problems.serializers import *


class UserSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
    class Meta:
        model = get_user_model()
        fields = ( 'id','username','email','password','is_superuser')

class UserProbSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserProb
        fields = '__all__'

class UserProbDetailSerializer(UserProbSerializers):
    p_type = ProbTypeSerializer(source='prob.pt_id')
    p_cate = ProbCateSerializer(source='prob.pc_id')
    class Meta(UserProbSerializers.Meta):
        fields = ('id', 'user', 'prob', 'date', 'correct', 'p_type', 'p_cate')