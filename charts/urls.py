from . import views
from django.urls import path

app_name = 'charts'

urlpatterns = [
    path('api/',views.chartAPI.as_view(), name="charts"),
] 