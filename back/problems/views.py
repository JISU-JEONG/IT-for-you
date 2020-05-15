from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from IPython import embed
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def get_prob(request):
  problems = ProblemBasic.objects.all()
  serializer = ProblemBasicSerializer(problems, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def problems_detail(request, problem_id):
  problem = get_object_or_404(ProblemBasic, pk=problem_id)
  # embed()
  serializer = ProblemAndAnswerSerializer(problem)
  # serializer = ProblemAndAnswerSerializer(problem)
  return Response(serializers.data)