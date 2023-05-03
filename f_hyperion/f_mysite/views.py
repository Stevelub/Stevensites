from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return HttpResponse("<h2>Hello World</h2>")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")