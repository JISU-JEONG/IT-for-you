from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from IPython import embed
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.
from rest_framework.views import APIView

# Read
@api_view(['GET'])
def get_prob_cate(request):
  prob_cates = ProbCate.objects.all()
  serializer = ProbCateSerializer(prob_cates, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_prob_type(request):
  prob_types = ProbType.objects.all()
  serializer = ProbTypeSerializer(prob_types, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_prob_diff(request):
  prob_diffs = ProbDiff.objects.all()
  serializer = ProbDiffSerializer(prob_diffs, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_probs(request):
  problems = Problem.objects.all()
  serializer = ProblemSerializer(problems, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_prob_by_id(request, problem_id):
  problem = get_object_or_404(Problem, pk=problem_id)
  serializer = ProblemDetailSerializer(problem)
  embed()
  return Response(serializer.data)

@api_view(['GET'])
def get_probs_detail(request):
  problems = Problem.objects.all()
  serializer = ProblemDetailSerializer(problems, many=True)
  return Response(serializer.data)

# Create
# @swagger_auto_schema(
#   method='post',
#   tags=['Problems'],
#   request_body=ProblemSerializer,
#   responses={200: openapi.Response(description='성공메세지', examples={'a': 'd'})}
# )
@api_view(['POST'])
def create_prob(request):
  # 문제 생성부
  problems = request.data.get('problems')
  # 키 이름 및 값 변경(pop) pc_value -> pc_id
  problems['pc_id'] = ProbCate.objects.get(pc_value=problems.pop('pc_value')).pc_id
  serializer = ProblemSerializer(data=problems)
  if serializer.is_valid(raise_exception=True):
    prob = serializer.save()

  # 보기 생성부
  answers = request.data.get('answers')
  ans_data = dict()
  ans_data['p_id'] = prob.p_id
  # 주관식(1), 단답식(4)
  if problems.get('pt_id') == 1 or problems.get('pt_id') == 4:
    ans_data['a_value'] = answers
    ans_data['a_correct'] = True
    serializer = AnswerSerializer(data=ans_data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
  # 객관식(2), OX Quiz(3)
  elif problems.get('pt_id') == 2 or problems.get('pt_id') == 3: 
    correct_ans = request.data.get('correct_ans')
    for ans in answers:
      ans_data['a_value'] = ans
      ans_data['a_correct'] = False
      if ans == correct_ans:
        ans_data['a_correct'] = True
      serializer = AnswerSerializer(data=ans_data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()

  return JsonResponse({'message': 'Success'})

# Update
@api_view(['PUT'])
def update_prob(request, prob_id):
  # Prob Update
  problems = request.data.get('problems')
  prob = get_object_or_404(Problem, p_id=prob_id)
  prob.p_question = problems.get('p_question')
  prob.p_code = problems.get('p_code')
  prob.pc_obj = ProbCate.objects.get(pc_value=problems.get('pc_value'))
  prob.pt_obj = ProbType.objects.get(pt_id=problems.get('pt_id'))
  prob.pd_obj = ProbDiff.objects.get(pd_id=problems.get('pd_id'))
  prob.save()

  # prob type이 바뀔 경우에 대비해 기존 기본 보기들 모두 삭제
  pre_answers = prob.answer_set.all()
  for ans in pre_answers:
    ans.delete()

  # 보기 생성부
  answers = request.data.get('answers')
  # 주관식(1), 단답식(4)
  if prob.pt_obj.pt_id == 1 or prob.pt_obj.pt_id == 4:
    a_value = answers
    a_correct = True
    answer = Answer(p_id=prob, a_value=a_value, a_correct=a_correct)
    answer.save()
  # 객관식(2), OX Quiz(3)
  elif prob.pt_obj.pt_id == 2 or prob.pt_obj.pt_id == 3: 
    correct_ans = request.data.get('correct_ans')
    for ans in answers:
      a_value = ans
      a_correct = False
      if a_value == correct_ans:
        a_correct = True
      # 외래키인 p_id는 숫자가 아닌 문제 객체 그 자체를 받아야 한다.
      answer = Answer(p_id=prob, a_value=a_value, a_correct=a_correct)
      answer.save()

  return JsonResponse({'message': 'Success'})


# Delete
@api_view(['DELETE'])
def prob_delete(request, prob_id):
  prob = Problem.objects.get(p_id=prob_id)
  prob.delete()
  return JsonResponse({'message': 'Success'})
