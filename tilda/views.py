from multiprocessing import context
from django.shortcuts import render
from .models import Category,Location,Image


# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render (request, 'photos/index.html',context)

def add(request):
    return render (request, 'photos/add.html')    

def view(request):
    return render (request, 'photos/view.html')
