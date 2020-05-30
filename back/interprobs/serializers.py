from rest_framework import serializers
from .models import Interview

class InterviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'