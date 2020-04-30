from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.permissions import AllowAny
from product.models import Product
from .serializers import ProductSerializer

class ProductList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
