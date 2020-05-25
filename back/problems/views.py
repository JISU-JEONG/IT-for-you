from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from IPython import embed
from .models import *
from accounts.models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status

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
  return Response(serializer.data)

@api_view(['GET'])
def get_probs_detail(request):
  problems = Problem.objects.all()
  serializer = ProblemDetailSerializer(problems, many=True)
  return Response(serializer.data)

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
  ans_data = dict()
  ans_data['p_id'] = prob.p_id
  answer = request.data.get('answer')
  # 객관식(2)
  if problems.get('pt_id') == 2:
    examples = request.data.get('examples')
    for example in examples:
      ans_data['a_value'] = example
      ans_data['a_correct'] = False
      if example == answer:
        ans_data['a_correct'] = True
      serializer = AnswerSerializer(data=ans_data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
  # 주관식(1), OX Quiz(3), 단답식(4)
  else:
    ans_data['a_value'] = answer
    ans_data['a_correct'] = True
    serializer = AnswerSerializer(data=ans_data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()

  return JsonResponse({'message': 'Success'})

# Update
@api_view(['PUT'])
def update_prob(request, prob_id):
  # Prob Update
  prob = get_object_or_404(Problem, p_id=prob_id)
  problems = request.data.get('problems')
  problems['pc_id'] = ProbCate.objects.get(pc_value=problems.pop('pc_value')).pc_id
  serializer = ProblemSerializer(data=problems, instance=prob)
  if serializer.is_valid(raise_exception=True):
    prob = serializer.save()

  # prob type이 바뀔 경우에 대비해 기존 기본 보기들 모두 삭제
  pre_answers = prob.answer_set.all()
  for ans in pre_answers:
    ans.delete()

  # 보기 생성부
  ans_data = dict()
  ans_data['p_id'] = prob.p_id
  answer = request.data.get('answer')
  # 객관식(2)
  if problems.get('pt_id') == 2:
    examples = request.data.get('examples')
    for example in examples:
      ans_data['a_value'] = example
      ans_data['a_correct'] = False
      if example == answer:
        ans_data['a_correct'] = True
      serializer = AnswerSerializer(data=ans_data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
  # 주관식(1), OX Quiz(3), 단답식(4)
  else:
    ans_data['a_value'] = answer
    ans_data['a_correct'] = True
    serializer = AnswerSerializer(data=ans_data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()

  return JsonResponse({'message': 'Success'})

# Delete
@api_view(['DELETE'])
def prob_delete(request, prob_id):
  prob = Problem.objects.get(p_id=prob_id)
  prob.delete()
  return JsonResponse({'message': 'Success'})

class TestProb(APIView):
  '''
  디폴트 설명인가?
  '''
  @swagger_auto_schema(
    tags=['Problem CRUD'],
  )
  def get(self, request):
    problems = Problem.objects.all()
    serializer = ProblemDetailSerializer(problems, many=True)
    return Response(serializer.data)

  @swagger_auto_schema(
    tags=['Problem CRUD'],
    request_body=ProbPostSerializer
  )
  def post(self, request):
    # 문제 생성부
    problems = request.data.get('problems')
    # 키 이름 및 값 변경(pop) pc_value -> pc_id
    problems['pc_id'] = ProbCate.objects.get(pc_value=problems.pop('pc_value')).pc_id
    serializer = ProblemSerializer(data=problems)
    if serializer.is_valid(raise_exception=True):
      prob = serializer.save()

    # 보기 생성부
    ans_data = dict()
    ans_data['p_id'] = prob.p_id
    answer = request.data.get('answer')
    # 객관식(2)
    if problems.get('pt_id') == 2:
      examples = request.data.get('examples')
      for example in examples:
        ans_data['a_value'] = example
        ans_data['a_correct'] = False
        if example == answer:
          ans_data['a_correct'] = True
        serializer = AnswerSerializer(data=ans_data)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
    # 주관식(1), OX Quiz(3), 단답식(4)
    else:
      ans_data['a_value'] = answer
      ans_data['a_correct'] = True
      serializer = AnswerSerializer(data=ans_data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response({'message': '작성 완료'}, status=status.HTTP_201_CREATED)
