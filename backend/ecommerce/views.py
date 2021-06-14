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
from .serializers                       import UserSerializer, LogoutSerializer

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

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
