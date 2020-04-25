from .views import *
from django.urls import path
app_name = 'accounts'

urlpatterns = [
    path('accounts/profile/',profile.as_view() ,name="profile"),
]