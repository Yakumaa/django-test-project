import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world, this is polls index")

def home(request):
    return render(request, 'home.html', {'name': 'home'})

def add(request):
    res1 = request.POST['num1']
    res2 = request.POST['num2']
    res = int(res1) + int(res2)
    return render(request, 'result.html', {'res': res})