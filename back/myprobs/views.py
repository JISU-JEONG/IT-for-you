from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from IPython import embed
from .models import *
from .serializers import *
# Create your views here.

class MyProblem(APIView):
    def get(self, request, user_id):
        myprobs = MyProb.objects.filter(user_id=user_id)
        serializer = MyProbListSerializer(myprobs, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        data = request.data
        data['user'] = user_id
        myprob = MyProb.objects.filter(user=user_id, prob=data.get('prob'))
        if myprob:
            myprob = get_object_or_404(MyProb, id=myprob[0].id)
            serializer = MyProbSerializer(data=data, instance=myprob)
        else:
            serializer = MyProbSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse({'message': 'Success'})

class MyProblemDetail(APIView):
    def get(self, request, user_id, myprob_id):
        myprob = get_object_or_404(MyProb, pk=myprob_id)
        serializers = MyProbDetailSerializer(myprob)
        return Response(serializers.data)

    def delete(self, request, user_id, myprob_id):
        myprob = get_object_or_404(MyProb, pk=myprob_id)
        myprob.delete()
        return JsonResponse({'message': 'Success'})