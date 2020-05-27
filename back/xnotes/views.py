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
# Create your views here.
# class Note(APIView):
#     @swagger_auto_schema(request_body=MyNoteSerializer)
#     def post(self, request):
#         serializer = MyNoteSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return JsonResponse({'message': 'Success'})

class MyNote(APIView):
    def get(self, request):
        mynotes = Xnote.objects.filter(user_id=request.data.get('user_id'))
        # embed()
        serializer = MyNoteListSerializer(mynotes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = XnoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse({'message': 'Success'})

class MyNoteDetail(APIView):
    def get(self, request, note_id):
        mynote = get_object_or_404(Xnote, pk=note_id)
        serializer = MyNoteDetailSerializer(mynote)
        return Response(serializer.data)
    
    def delete(self, request, note_id):
        mynote = get_object_or_404(Xnote, pk=note_id)
        mynote.delete()
        return JsonResponse({'message': 'Success'})

# class MyNote2(APIView):
#     def get(self, request, user_id, prob_id):
#         pass
        
#     def post(self, request, user_id, prob_id):
#         # embed()
#         mynotes = Xnote.objects.filter(user_id=user_id, prob_id=prob_id)
#         if mynotes:
#             mynotes.delete()

#         serializer = MyNoteSerializer(data={'u_answer': request.data.get('u_answer'), 'user': user_id, 'prob': prob_id})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return JsonResponse({'message': 'Success'})

#     def delete(self, request, user_id, prob_id):
#         embed()
#         mynote = get_object_or_404(Xnote, user_id=user_id)
        