from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from IPython import embed
from .models import *
from accounts.models import *
from .serializers import *
from myprobs.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from django.db.models import Q
import random
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
    
    if problems.get('pt_id') == 1:
      problems['p_commentary'] = request.data.get('answer')
      serializer = ProblemSerializer(data=problems)
      if serializer.is_valid(raise_exception=True):
        prob = serializer.save()
    # 보기 생성부
    else:
      serializer = ProblemSerializer(data=problems)
      if serializer.is_valid(raise_exception=True):
        prob = serializer.save()
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
      # OX Quiz(3)
      elif problems.get('pt_id') == 3:
        ox = ['O', 'X']
        for i in ox:
          if answer == i:
            ans_data['a_correct'] = True
          else:
            ans_data['a_correct'] = False
          ans_data['a_value'] = i
          serializer = AnswerSerializer(data=ans_data)
          if serializer.is_valid(raise_exception=True):
            serializer.save()
      # 단답식(4)
      elif problems.get('pt_id') == 4:
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
    if problems.get('pt_id') == 1:
      problems['p_commentary'] = request.data.get('answer')

    serializer = ProblemSerializer(data=problems, instance=prob)
    if serializer.is_valid(raise_exception=True):
      prob = serializer.save()

    # prob type이 바뀔 경우에 대비해 기존 기본 보기들 모두 삭제
    pre_answers = prob.answer_set.all()
    for ans in pre_answers:
      ans.delete()

    if problems.get('pt_id') != 1:
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
      # OX Quiz(3), 단답식(4)
      else:
        ans_data['a_value'] = answer
        ans_data['a_correct'] = True
        serializer = AnswerSerializer(data=ans_data)
        if serializer.is_valid(raise_exception=True):
          serializer.save()

    return JsonResponse({'message': 'Success'})

  # Delete
  def delete(self, request, problem_id):
    prob = get_object_or_404(Problem, p_id=problem_id)
    prob.delete()
    return JsonResponse({'message': 'Success'})

class ProbSearch(APIView):
  @swagger_auto_schema(tags=['Problem Search'])
  def post(self, request):
    user_id = request.data.get('user_id')
    pd_id = request.data.get('pd_id')
    pc_id = []
    p_number = request.data.get('p_number')
    for cate in request.data.get('pc_value'):
      pc_id.append(ProbCate.objects.get(pc_value=cate).pc_id)
    
    if not pc_id:
      pc_id = [i for i in range(1, len(ProbCate.objects.all()) + 1)]
    if not pd_id:
      pd_id = [i for i in range(1, len(ProbDiff.objects.all()) + 1)]
    
    problems = Problem.objects.exclude(pt_id=1)
    problems = problems.filter(pc_id__in=pc_id, pd_id__in=pd_id)

    random_index = [prob.p_id for prob in problems]
    if len(problems) > p_number:
      random_index = random.sample(random_index, p_number)
      problems = Problem.objects.filter(p_id__in=random_index)
    else:
      random_index = random.sample(random_index, len(problems))
      problems = Problem.objects.filter(p_id__in=random_index)
      
    serializer = ProblemDetailSerializer(problems, many=True, context={'user_id': user_id})

    return Response(serializer.data)
    