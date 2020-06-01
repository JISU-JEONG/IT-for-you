from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.

class MyProb(APIView):
    def get(self, request, user_id):
        myprobs = MyProb.objects.filter(user_id=user_id)