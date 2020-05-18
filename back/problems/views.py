from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from IPython import embed
from .models import *
from .serializers import *
# Create your views here.

# Read
@api_view(['GET'])
def get_probs(request):
  problems = ProblemBasic.objects.all()
  serializer = ProblemBasicSerializer(problems, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_prob_by_id(request, problem_id):
  problem = get_object_or_404(ProblemBasic, pk=problem_id)
  serializer = ProblemAndAnswerSerializer(problem)
  return Response(serializer.data)

@api_view(['GET'])
def get_probs_detail(request):
  problems = ProblemBasic.objects.all()
  serializer = ProblemAndAnswerSerializer(problems, many=True)
  return Response(serializer.data)

# Create
@api_view(['POST'])
def create_prob(request):
  prob_info = request.data.get('problems')
  
  
  # 문제 생성부
  p_category = prob_info.get('p_category')
  p_question = prob_info.get('p_question')
  p_type = prob_info.get('p_type')
  p_diff = prob_info.get('p_diff')
  prob = ProblemBasic(p_category=p_category, p_question=p_question, p_type=p_type, p_diff=p_diff)
  prob.save()

  # 보기 생성부
  # prob_id = prob.p_id
  
  return JsonResponse({'message': 'Success'})
  
  
def create_ans(request, prob_pk):
  ans_list = request.data.get('answers')
  correct_ans = request.data.get('answers')
  for ans_idx in range(len(ans_list)):
    p_id = prob_pk
    a_value = ans_list

