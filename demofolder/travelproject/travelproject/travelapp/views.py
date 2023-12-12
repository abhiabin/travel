from django.shortcuts import render
from django.http import HttpResponse
from.models import place
from .models import itemss
# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1=itemss.objects.all()
    return render(request, "index.html", {"result": obj,"res":obj1})






