from django.shortcuts import render
from django.http import JsonResponse

def charts(request):
    labels = ["java","js","python","GO"]
    data = [90,45,180,45]
    return render(request, 'charts.html',{
        'labels': labels,
        'data': data,
    })