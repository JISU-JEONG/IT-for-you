from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from IPython import embed
from .models import *
from accounts.models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
# Create your views here.


@swagger_auto_schema(method='get', tags=['Problem Basic Info'])
@api_view(['GET'])
def get_prob_cate(request):
  prob_cates = ProbCate.objects.all()
  serializer = ProbCateSerializer(prob_cates, many=True)
  return Response(serializer.data)

@swagger_auto_schema(method='get', tags=['Problem Basic Info'])
@api_view(['GET'])
def get_prob_type(request):
  prob_types = ProbType.objects.all()
  serializer = ProbTypeSerializer(prob_types, many=True)
  return Response(serializer.data)

@swagger_auto_schema(method='get', tags=['Problem Basic Info'])
@api_view(['GET'])
def get_prob_diff(request):
  prob_diffs = ProbDiff.objects.all()
  serializer = ProbDiffSerializer(prob_diffs, many=True)
  return Response(serializer.data)

# 모든 문제 GET / 문제 생성 POST
class Prob(APIView):
  def get(self, request):
    problems = Problem.objects.all()
    serializer = ProblemDetailSerializer(problems, many=True)
    return Response(serializer.data)

  @swagger_auto_schema(request_body=ProbPostSerializer, responses={201: '문제 생성'})
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

    return JsonResponse({'message': 'Success'})

# Specific Problem
class SpecProb(APIView):
  def get(self, request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    serializer = ProblemDetailSerializer(problem)
    return Response(serializer.data)
  
  # Update
  @swagger_auto_schema(request_body=ProbPostSerializer, responses={200: '문제 수정'})
  def put(self, request, problem_id):
    # Prob Update
    prob = get_object_or_404(Problem, p_id=problem_id)
    problems = request.data.get('problems')
    problems['pc_id'] = ProbCate.objects.get(pc_value=problems.pop('pc_value')).pc_id

    if prob.p_code:
      prob.p_code = None

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
  def delete(self, request, problem_id):
    prob = Problem.objects.get(p_id=problem_id)
    prob.delete()
    return JsonResponse({'message': 'Success'})
