from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from .models import User
from problems.models import Problem
from .serializers import *
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from IPython import embed
from rest_framework.views import APIView
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

@api_view(['DELETE'])
def user_delete(request, user_id):
    token = request.headers['Authorization'][4:]
    user_info = VerifyJSONWebTokenSerializer().validate({'token': token})['user']
    if user_info.is_superuser or user_info.id == user_id:
        user = get_object_or_404(User, id=user_id)
        if user.is_superuser:
            return Response({'message': '관리자 삭제 불가'})
        else:
            user.delete()
            return Response({'message': '삭제되었습니다.'})
    return Response({'message': '권한이 없습니다.'})

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


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializers = UserSerializers(users, many = True)
    return Response(serializers.data)


class SaveProb(APIView):
    def get(self, request):
        token = request.headers['Authorization'][4:]
        user_info = VerifyJSONWebTokenSerializer().validate({'token': token})['user']
        query_data = request.query_params
        if user_info.id == int(query_data['user_id']):
            if query_data.get('date'):
                user_prob = UserProb.objects.filter(user_id=query_data['user_id'], date=query_data['date'])
            else:
                user_prob = UserProb.objects.filter(user_id=query_data['user_id'])
            serializer = UserProbDetailSerializer(user_prob, many=True)
            return Response(serializer.data)
        return Response({'message': '권한이 없습니다.'})


    def post(self, request):
        token = request.headers['Authorization'][4:]
        user_info = VerifyJSONWebTokenSerializer().validate({'token': token})['user']
        if user_info.id == request.data.get('user'):
            serializer = UserProbSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response({'message': '저장되었습니다.'}) 
        return Response({'message': '권한이 없습니다.'}) 
