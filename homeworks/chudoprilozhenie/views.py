from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("<h1>Hello! It is my first view!</h1>")

def second_view(request):
    return HttpResponse("<h1>Hello! It is my second view!</h1>")
