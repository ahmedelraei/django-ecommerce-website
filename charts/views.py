from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Category

""" def charts(request):
    labels = ["java","js","python","GO"]
    data = [90,45,180,45]
    return render(request, 'charts.html',{
        'labels': labels,
        'data': data,
    }) """

class chartAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):
        categories = Category.objects.all()
        labels = []
        for cat in categories:
            labels.append(cat.CATname)
        data = [1500,1000,2000,500,805]
        mainLabel = "views"
        chartType = "bar"   
        response = {
            "labels":labels,
            "data":data,
            "mainLabel":mainLabel,
            "chartType": chartType,
        }
        return Response(response)