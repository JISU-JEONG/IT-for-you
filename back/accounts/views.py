from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User

# Create your views here.
@api_view()
def user_login(requset):
    pass