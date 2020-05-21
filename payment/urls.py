from .views import *
from django.urls import path , include

app_name = 'payment'

urlpatterns = [
    path('process/',payment_process ,name="process"),
    path('success/',payment_done ,name="success"),
    path('failed/',payment_canceled ,name="failed"),


]