from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def get_prob(request):
  problems = ProblemBasic.objects.all()
  serializer = ProblemBasicSerializer(problems, many=True)
  return Response(serializer.data)

# @api_view(['POST'])
# def create_prob(request):
  