from .views import *
from django.urls import path

app_name = 'clients'

urlpatterns = [
    path('product-list/',ProductListAPI.as_view() ,name="productListAPI"),
    path('categories-list/',CategoryListAPI.as_view() ,name="categoryListAPI"),

]