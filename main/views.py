from django.shortcuts import render
from djando.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>home</h1>")
