from django.shortcuts import render
from django.core import serializers
from rest_framework import status, viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt

from rest_framework.parsers import JSONParser 
from rest_framework import generics, permissions, mixins, viewsets

from django.db.models import Count, Sum

from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class LoginAPI(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        pass

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]