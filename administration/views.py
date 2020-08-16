from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Logo
from django.http import JsonResponse

@staff_member_required
def dashboard(request):

    return render(request, 'dashboard.html',{})

def SiteData(request):
    logo = Logo.objects.all()[0]
    return JsonResponse({'logo':logo.get_absolute_image_url()})