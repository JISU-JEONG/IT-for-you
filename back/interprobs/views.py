from django.shortcuts import render, get_object_or_404
from .models import Interview
from accounts.models import *
from .serializers import *
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
import speech_recognition as sr
import os
import base64
import json
# Create your views here.

class InterSearch(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        pc_id = ProbCate.objects.get(pc_value=request.data.get('category')).pc_id
        interprobs = Problem.objects.filter(pt_id=1, pc_id=pc_id)
        # embed()
        serializer = InterprobDetailSerializer(interprobs, many=True, context={'user_id': user_id})
        return Response(serializer.data)


class InterRecord(APIView):
    def post(self, request):
        token = request.headers['Authorization'][4:]
        user_info = VerifyJSONWebTokenSerializer().validate({'token': token})['user']
        if not request.data.get('body'):
            audio = request.data['audio']
            r = sr.Recognizer()
            with sr.AudioFile(audio) as source:
                audio_source = r.record(source) 
            text = r.recognize_google(audio_data = audio_source,language = "ko-KR")
            return Response({'content': text})
        elif request.data.get('body'):
            data = json.loads(request.data.get('body'))
            data['user'] = user_info.id
            data['file'] = request.data.get('audio')
            interview = Interview.objects.filter(user=data['user'], prob=data['prob'])
            if interview:
                interview = interview[0]
                os.remove(interview.file.path)
                serializer = InterviewSerializers(data=data, instance=interview)
            else:
                serializer = InterviewSerializers(data=data)

            if serializer.is_valid(raise_exception=True):
                interview = serializer.save()
                interview.path = interview.file.path
                interview.save()

            return Response({'message': '생성되었습니다.'})
# @api_view(['GET'])
# def ViewInterviews(request):
#     interviews = Interview.objects.all()
#     serializers = InterviewSerializers(interviews,many=True)
#     return Response(serializers.data)

# @api_view(['POST'])
# def voice(request):
#     audio = request.data['audio']
#     r = sr.Recognizer()
#     with sr.AudioFile(audio) as source:
#         audio_source = r.record(source) 
#     text = r.recognize_google(audio_data = audio_source,language = "ko-KR")
#     user = get_object_or_404(User, pk=1)
#     prob = get_object_or_404(Problem, p_id=2)
#     interview = Interview.objects.filter(user=user.pk).filter(prob=prob.p_id)
#     if interview:
#         interview = interview[0]
#         os.remove(interview.file.path)
#         interview.content = text
#         interview.file = audio
#         interview.save()
#     else:
#         interview = Interview()
#         interview.user = user
#         interview.prob = prob
#         interview.content = text
#         interview.file = audio
#         interview.save()
#     interview.path = interview.file.path
#     interview.save()
#     return Response({'message': '추가되었습니다.'})

# @api_view(['POST'])
# def get_interview(request, p_id):
#     data = request.data
#     valid_data = VerifyJSONWebTokenSerializer().validate(data)
#     user = valid_data['user']
#     prob = get_object_or_404(Problem, p_id=p_id)
#     interview = Interview.objects.filter(user=user.pk).filter(prob=prob.p_id)[0]
#     serializers = InterviewSerializers(interview)
#     return Response(serializers.data)


# @api_view(['POST'])
# def get_audio(request, p_id):
#     data = request.data
#     valid_data = VerifyJSONWebTokenSerializer().validate(data)
#     user = valid_data['user']
#     prob = get_object_or_404(Problem, p_id=p_id)
#     interview = Interview.objects.filter(user=user.pk).filter(prob=prob.p_id)[0]
#     audio_data = interview.file.read()
#     audio_data = 'data:audio/mpeg;base64,' + base64.b64encode(audio_data).decode('utf-8')
#     return HttpResponse(audio_data)





class MyInterview(APIView):
    def get(self, request, user_id):
        myinters = Interview.objects.filter(user_id=user_id)
        serializer = MyInterListSerializers(myinters, many=True)
        return Response(serializer.data)

class MyInterviewDetail(APIView):
    def get(self, request, user_id, myinter_id):
        myinter = get_object_or_404(Interview,id=myinter_id)
        serializer = MyInterDetailSerializers(myinter)
        return Response(serializer.data)

    def delete(self, request, user_id, myinter_id):
        token = request.headers['Authorization'][4:]
        user_info = VerifyJSONWebTokenSerializer().validate({'token': token})['user']
        if user_id == user_info.id or user_info.is_superuser:
            myinter = get_object_or_404(Interview, id=myinter_id)
            os.remove(myinter.file.path)
            myinter.delete()
            return Response({'message': '삭제완료'})
        else:
            return Response({'message': '권한이 없습니다.'})