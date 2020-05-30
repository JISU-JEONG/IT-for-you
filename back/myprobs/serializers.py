from rest_framework import serializers
from .models import *

class MyProbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProb
        fields = ('id', 'user', 'prob',)