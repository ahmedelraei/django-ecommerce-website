from .views import *
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'clients'

urlpatterns = [
    path('product-list/<query>/',ProductListAPI.as_view() ,name="productListAPI"),
    path('categories-list/',CategoryListAPI.as_view() ,name="categoryListAPI"),
    path('order-list/',OrderAPI.as_view() ,name="orderListAPI"),
    path('token/',obtain_auth_token,name="obtain-token"),
]