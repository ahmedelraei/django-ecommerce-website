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
            return Product.objects.filter(
            Q(PRDname__icontains=kw['query']) | Q(PRDdesc__icontains=kw['query'])
            | Q(PRDcategory__CATname__icontains=kw['query'])
            )

        elif filter == 'low-high':
            return Product.objects.filter(
            Q(PRDname__icontains=kw['query']) | Q(PRDdesc__icontains=kw['query'])
            | Q(PRDcategory__CATname__icontains=kw['query'])
            ).order_by('PRDprice')
        
        elif filter == 'high-low':
            return Product.objects.filter(
            Q(PRDname__icontains=kw['query']) | Q(PRDdesc__icontains=kw['query'])
            | Q(PRDcategory__CATname__icontains=kw['query'])
            ).order_by('-PRDprice')

        elif filter == 'trending':
            return Product.objects.filter(
            Q(PRDname__icontains=kw['query']) | Q(PRDdesc__icontains=kw['query']) | Q(PRDcategory__CATname__icontains=kw['query']),
            PRDisTrend=True
            )
        elif filter == 'new':
            return Product.objects.filter(
            Q(PRDname__icontains=kw['query']) | Q(PRDdesc__icontains=kw['query']) | Q(PRDcategory__CATname__icontains=kw['query']),
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

