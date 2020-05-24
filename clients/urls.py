from .views import *
from django.urls import path

app_name = 'clients'

urlpatterns = [
    path('accounts/profile/',profile.as_view() ,name="profile"),
    path('accounts/edit-address/<pk>',EditAddress.as_view() ,name="edit-address"),
    path('track-order/',trackOrderView.as_view() ,name="track-order"),
    #path('track-order/ref/',trackOrder ,name="track-order-result"),
    path('cancel-order/<code>',CancelOrder.as_view() ,name="cancel-order"),
]