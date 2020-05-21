from django.contrib import admin
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "street_address",
        "address2",
        "zipCode",
        "country",
        "city"
    )
    search_fields = (
        "user__username",
        "street_address",
        "address2",
        "zipCode",
        "country",
        "city",
        )

admin.site.register(Address,AddressAdmin)
admin.site.register(Profile)


