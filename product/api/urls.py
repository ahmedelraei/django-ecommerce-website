from django.urls import path
from .views import ProductList
urlpatterns = [
    path('product-list/',ProductList.as_view(), name='product-list')
]