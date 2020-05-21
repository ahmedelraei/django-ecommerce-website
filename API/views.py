from django.shortcuts import render
from .serializers import ProductSerializer , CategorySerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from product.models import Product , Category

class ProductListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CategoryListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()