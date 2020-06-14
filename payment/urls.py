from .views import *
from django.urls import path , include

app_name = 'payment'

urlpatterns = [
    path('e-wallet/',PAY_eWallet.as_view() ,name="e-wallet"),

]