from django.contrib import admin
from .models import *

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','amount','payment_type')

    
admin.site.register(Payment,PaymentAdmin)
