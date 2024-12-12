from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World : Django Project01 Test:home")

def about(request):
    return HttpResponse("Hello, World : Django Project01 Test:about")

def contact(request):
    return HttpResponse("Hello, World : Django Project01 Test:contact")