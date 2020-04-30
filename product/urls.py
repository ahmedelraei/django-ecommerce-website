from .views import *
from django.urls import path , include
app_name = 'product'

urlpatterns = [
    path('',home ,name="home"),
    path('products/',product_list.as_view(), name="product_list"),
    path('products/<slug:slug>',product_details ,name="product_details"),
    path('categories/<slug:slug>',cat.as_view(),name="category"),
    path('cart/',cart.as_view(),name="cart"),
    path('categories/sub/<slug:slug>',subCategory.as_view() ,name="sub-category"),
    path('add-to-cart/<slug:slug>',addToCart,name="add-to-cart"),
    path('increase-cart/<slug:slug>',increaseCart,name="increase-cart"),
    path('remove-from-cart/<slug:slug>',removeFromCart,name="remove-from-cart"),
    path('decrease-cart/<slug:slug>',decreaseFromCart,name="decrease-cart"),
    path('checkout/',checkout.as_view(),name="checkout"),
    path('payment/<payment_option>',PaymentView.as_view(),name="payment"),
    path('api/',include('product.api.urls')),
]