from .views import *
from django.urls import path , include

app_name = 'designer'

urlpatterns = [
    path('',editorView.as_view() ,name="editor"),

]