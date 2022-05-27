from django.shortcuts import render,request
from django.http  import HttpResponse


# Create your views here.
def home(request):
    return request('Welcome to tilda app')
