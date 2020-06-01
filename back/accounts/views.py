from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from .models import User
from problems.models import Problem
from .serializers import UserSerializers

from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from IPython import embed
from interprobs.models import Interview
from interprobs.serializers import InterviewSerializers
import speech_recognition as sr

import os

# Create your views here.
@api_view(['POST'])
def user_signup(request):
    serializers = UserSerializers(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
        return Response(serializers.data)

@api_view(['POST', 'PUT'])
def user(request):
    
    if request.method == 'POST':
        headers = request.headers
        token = headers["Authorization"][4:]
        valid_data = VerifyJSONWebTokenSerializer().validate({'token' : token})
        user = valid_data['user']
        serializers = UserSerializers(user)
        return Response(serializers.data)
    
    # elif request.method == 'PUT':
    #     serializers = UserSerializers(data=request.data,instance=user)
    #     if serializers.is_valid(raise_exception=True):
    #         serializers.save()
    #         return Response(serializers.data)

@api_view(['POST'])
def user_delete(request):
    if request.method == 'POST':
        data = request.data
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']
        user.delete()
        return Response({'message': '삭제되었음'})

# @api_view(['POST'])
# def add_problem(request, problem_pk):
#     data = request.data
#     valid_data = VerifyJSONWebTokenSerializer().validate(data)
#     user = valid_data['user']
#     problem = get_object_or_404(Problem, pk=problem_pk)

#     if problem in user.uncorrets.all():
#         user.uncorrets.remove(problem)
#     else:
#         user.uncorrets.add(problem)
@api_view(['POST'])
def voice(request):
    print('들어옴')
    audio = request.data['audio']
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_source = r.record(source) 
    text = r.recognize_google(audio_data = audio_source,language = "ko-KR")
    user = get_object_or_404(User, pk=1)
    prob = get_object_or_404(Problem, p_id=2)
    interview = Interview.objects.filter(user=user.pk).filter(prob=prob.p_id)
    if interview:
        interview = interview[0]
        os.remove(interview.file.path)
        interview.content = text
        interview.file = audio
        interview.save()
    else:
        interview = Interview()
        interview.user = user
        interview.prob = prob
        interview.content = text
        interview.file = audio
        interview.save()
    interview.path = interview.file.path
    interview.save()
    return Response({'message': '추가되었습니다.'})

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializers = UserSerializers(users, many = True)
    return Response(serializers.data)

@api_view(['POST'])
def get_interview(request, p_id):
    data = request.data
    valid_data = VerifyJSONWebTokenSerializer().validate(data)
    user = valid_data['user']
    prob = get_object_or_404(Problem, p_id=p_id)
    interview = Interview.objects.filter(user=user.pk).filter(prob=prob.p_id)[0]
    serializers = InterviewSerializers(interview)
    # serializers.path = serializers.file.path
    # serializers.save()
    return Response(serializers.data)