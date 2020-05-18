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
  # 문제 생성부
  prob_info = request.data.get('problems')
  p_category = prob_info.get('p_category')
  p_question = prob_info.get('p_question')
  p_type = prob_info.get('p_type')
  p_diff = prob_info.get('p_diff')
  prob = ProblemBasic(p_category=p_category, p_question=p_question, p_type=p_type, p_diff=p_diff)
  # embed()
  prob.save()
  # 보기 생성부
  answers = request.data.get('answers')
  correct_ans = request.data.get('correct_ans')
  for ans in answers:
    # embed()
    a_value = ans
    a_correct = False
    if a_value == correct_ans:
      a_correct = True
    # 외래키인 p_id는 숫자가 아닌 문제 객체 그 자체를 받아야 한다.
    answer = AnswerBasic(p_id=prob, a_value=a_value, a_correct=a_correct)
    answer.save()

  return JsonResponse({'message': 'Success'})
  
# Update
@api_view(['PUT'])
def update_prob(request, prob_id):
  # Prob Update
  prob_info = request.data.get('problems')
  prob = get_object_or_404(ProblemBasic, p_id=prob_id)
  prob.p_category = prob_info.get('p_category')
  prob.p_question = prob_info.get('p_question')
  prob.p_type = prob_info.get('p_type')
  prob.p_diff = prob_info.get('p_diff')
  prob.save()

  # Answer Update
  new_answers = request.data.get('answers')
  new_correct_ans = request.data.get('correct_ans')
  pre_answers = prob.answerbasic_set.all()
  for ans_idx in range(len(new_answers)):
    ans = get_object_or_404(AnswerBasic, a_id=pre_answers[ans_idx].a_id)
    ans.a_value = new_answers[ans_idx]
    ans.a_correct = False
    if ans.a_value == new_correct_ans:
      ans.a_correct = True
    ans.save()

  return JsonResponse({'message': 'Success'})


# Delete
@api_view(['DELETE'])
def prob_delete(request, prob_id):
  prob = ProblemBasic.objects.get(p_id=prob_id)
  prob.delete()
  return JsonResponse({'message': 'Success'})
