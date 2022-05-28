from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def home(request):
    return render (request, 'index.html')

def add(request):
    return render (request, 'add.html')    

def view(request):
    return render (request, 'view.html')
