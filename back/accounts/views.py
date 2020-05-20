from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializers

# Create your views here.
@api_view(['POST'])
def user_signup(request):
    serializers = UserSerializers(data=request.data)
    print(serializers)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
        return Response(serializers.data)
    
