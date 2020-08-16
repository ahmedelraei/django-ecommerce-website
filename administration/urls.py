from .views import *
from django.urls import path , include

app_name = 'administration'

urlpatterns = [
    path('dashboard/',dashboard ,name="dashboard"),
    path('site-data/',SiteData, name="site-data")

]