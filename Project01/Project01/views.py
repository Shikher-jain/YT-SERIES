from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World : Django Project01 Test:home")
    return render(request,"website/index.html")

def about(request):
    return HttpResponse("Hello, World : Django Project01 Test:about")

def contact(request):
    return HttpResponse("Hello, World : Django Project01 Test:contact")

