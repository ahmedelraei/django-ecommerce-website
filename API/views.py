from django.shortcuts import render
from .serializers import ProductSerializer , CategorySerializer , OrderSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAdminUser
from product.models import Product , Category , Order
from django.db.models import Q

class ProductListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        kw = self.kwargs
        filter = self.request.GET.get('filter')
        if kw['query'] == 'all':
            return Product.objects.all()

        if filter == None:
            query = kw['query'].replace('-',' ')
            return Product.objects.filter(
            Q(PRDname__icontains=query) | Q(PRDdesc__icontains=query)
            | Q(PRDcategory__CATname__icontains=query)
            )

        elif filter == 'low-high':
            query = kw['query'].replace('-',' ')
            return Product.objects.filter(
            Q(PRDname__icontains=query) | Q(PRDdesc__icontains=query)
            | Q(PRDcategory__CATname__icontains=query)
            ).order_by('PRDprice')
        
        elif filter == 'high-low':
            query = kw['query'].replace('-',' ')
            return Product.objects.filter(
            Q(PRDname__icontains=query) | Q(PRDdesc__icontains=query)
            | Q(PRDcategory__CATname__icontains=query)
            ).order_by('-PRDprice')

        elif filter == 'trending':
            query = kw['query'].replace('-',' ')
            return Product.objects.filter(
            Q(PRDname__icontains=query) | Q(PRDdesc__icontains=query) | Q(PRDcategory__CATname__icontains=query),
            PRDisTrend=True
            )
        elif filter == 'new':
            query = kw['query'].replace('-',' ')
            return Product.objects.filter(
            Q(PRDname__icontains=query) | Q(PRDdesc__icontains=query) | Q(PRDcategory__CATname__icontains=query),
            PRDisNew=True
            )

class CategoryListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class OrderAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        order_ref = self.request.GET.get('order_ref')

        if order_ref:
            return Order.objects.filter(
                order_ref=order_ref
            )

