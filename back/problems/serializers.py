from rest_framework import serializers
from .models import *
class ProblemBasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProblemBasic
    fields = '__all__'