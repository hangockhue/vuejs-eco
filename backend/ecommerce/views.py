from django.shortcuts import render, get_object_or_404
from django.core import serializers
from rest_framework import status, viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt

from rest_framework.parsers import JSONParser 
from rest_framework import generics, permissions, mixins, viewsets

from django.db.models                   import Count, Sum
from django.contrib.auth.models         import User
from django.core.paginator              import Paginator
from rest_framework.pagination          import PageNumberPagination
from .serializers                       import UserSerializer


class LoginAPI(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        pass

class UserAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_object(self):
        # queryset            = User.objects.all()
        # serializer_class    = UserSerializer
        pk = self.kwargs["pk"]
        return get_object_or_404(User, pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)