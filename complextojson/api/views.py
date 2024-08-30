from django.shortcuts import render
from .models import Cafe
from .serializers import CafeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def showorderDetail(request):
    ord = Cafe.objects.get(id=2)
    serializer = CafeSerializer(ord)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')
