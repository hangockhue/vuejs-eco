from django.shortcuts import render
from django.core import serializers
from rest_framework import status, viewsets, views
from .models import Category, Product, Order
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CategorySerializer, ProductSerializer , OrderSerializer

from rest_framework.parsers import JSONParser 
from rest_framework import generics, permissions, mixins, viewsets

from django.db.models import Count, Sum

from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination

class CategoryViewSet(generics.GenericAPIView, mixins.ListModelMixin,):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class OrderViewSet(generics.GenericAPIView, mixins.ListModelMixin):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductViewSet(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    ):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    queryset = Product.objects.all()    
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer