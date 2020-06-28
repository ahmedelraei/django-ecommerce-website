from .views import *
from django.urls import path , include
app_name = 'product'

urlpatterns = [
    path('',home ,name="home"),
    path('products/<str:str>',product_details ,name="product_details"),
    path('cart/',cart.as_view(),name="cart"),
    path('add-to-cart/<str:str>',addToCart,name="add-to-cart"),
    path('increase-cart/<str:str>',increaseCart,name="increase-cart"),
    path('remove-from-cart/<str:str>',removeFromCart,name="remove-from-cart"),
    path('decrease-cart/<str:str>',decreaseFromCart,name="decrease-cart"),
    path('checkout/',checkout.as_view(),name="checkout"),
    path('s/',search, name="search"),

]