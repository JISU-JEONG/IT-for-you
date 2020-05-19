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

# # Create
@api_view(['POST'])
def create_prob(request):
  # 문제 생성부
  problems = request.data.get('problems')
  p_question = problems.get('p_question')
  pc_id = ProbCate.objects.get(pc_value=problems.get('pc_value'))
  pt_id = ProbType.objects.get(pt_id=problems.get('pt_id'))
  pd_id = ProbDiff.objects.get(pd_id=problems.get('pd_id'))
  prob = Problem(p_question=p_question, pc_id=pc_id, pt_id=pt_id, pd_id=pd_id)
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
    answer = Answer(p_id=prob, a_value=a_value, a_correct=a_correct)
    answer.save()

  return JsonResponse({'message': 'Success'})

# # Update
# @api_view(['PUT'])
# def update_prob(request, prob_id):
#   # Prob Update
#   prob_info = request.data.get('problems')
#   prob = get_object_or_404(Problem, p_id=prob_id)
#   prob.p_category = prob_info.get('p_category')
#   prob.p_question = prob_info.get('p_question')
#   prob.p_type = prob_info.get('p_type')
#   prob.p_diff = prob_info.get('p_diff')
#   prob.save()

#   # Answer Update
#   new_answers = request.data.get('answers')
#   new_correct_ans = request.data.get('correct_ans')
#   pre_answers = prob.answerbasic_set.all()
#   for ans_idx in range(len(new_answers)):
#     ans = get_object_or_404(Answer, a_id=pre_answers[ans_idx].a_id)
#     ans.a_value = new_answers[ans_idx]
#     ans.a_correct = False
#     if ans.a_value == new_correct_ans:
#       ans.a_correct = True
#     ans.save()

#   return JsonResponse({'message': 'Success'})


# # Delete
# @api_view(['DELETE'])
# def prob_delete(request, prob_id):
#   prob = Problem.objects.get(p_id=prob_id)
#   prob.delete()
#   return JsonResponse({'message': 'Success'})
