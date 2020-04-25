from . import views
from django.urls import path

app_name = 'charts'

urlpatterns = [
    path('',views.charts, name="charts"),
] 