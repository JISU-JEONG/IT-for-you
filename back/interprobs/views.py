from django.shortcuts import render
from .models import Interview
from .serializers import InterviewSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def ViewInterviews(request):
    interviews = Interview.objects.all()
    serializers = InterviewSerializers(interviews,many=True)
    return Response(serializers.data)