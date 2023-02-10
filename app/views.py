from django.shortcuts import render
from .models import Progression
# Create your views here.


def index(request):
    return render(request,'index.html')

def auth1(request):
    df  = {
        'prog':Progression.objects.all()
    }
    return render(request,'auth1.html',df)

def auth2(request):
    return render(request,'auth2.html')

def auth3(request):
    return render(request,'auth3.html')

def main1(request):
    df2  = {
        'prog':Progression.objects.all()
    }
    
    return render(request,'main1.html',df2)

def main1_1(request):
    df3  = {
        'prog':Progression.objects.all()
    }
    return render(request,'main1_1.html',df3)

def main2(request):
    return render(request,'main2.html')

def main2_1(request):
    return render(request,'main2_1.html')

def main3(request):
    return render(request,'main3.html')