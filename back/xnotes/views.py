from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from IPython import embed
from .models import *
from problems.models import *
from problems.serializers import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema

class MyNote(APIView):
    def get(self, request, user_id):
        mynotes = Xnote.objects.filter(user_id=user_id)
        serializer = MyNoteListSerializer(mynotes, many=True)
        return Response(serializer.data)
    
    def post(self, request, user_id):
        data = request.data
        data['user'] = user_id
        mynote = Xnote.objects.filter(user=user_id, prob=data.get('prob'))
        if mynote:
            mynote = get_object_or_404(Xnote, id=mynote[0].id)
            serializer = XnoteSerializer(data=data, instance=mynote)
        else:
            serializer = XnoteSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse({'message': 'Success'})

class MyNoteDetail(APIView):
    def get(self, request, user_id, note_id):
        mynote = get_object_or_404(Xnote, pk=note_id)
        serializer = MyNoteDetailSerializer(mynote)
        return Response(serializer.data)
    
    def delete(self, request, user_id, note_id):
        mynote = get_object_or_404(Xnote, pk=note_id)
        mynote.delete()
        return JsonResponse({'message': 'Success'})
