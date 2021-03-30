from django.shortcuts import render
from django.core import serializers
from rest_framework import status, viewsets, views
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import generics, permissions, mixins, viewsets

from rest_framework_simplejwt.views import TokenViewBase, TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
