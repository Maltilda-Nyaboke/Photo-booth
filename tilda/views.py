from multiprocessing import context
from django.shortcuts import render
from .models import Category,Location,Image


# Create your views here.
def home(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    locations = Location.objects.all()
    context = {
        'categories': categories,
        'images': images,
        'locations': locations,
    }
    return render (request, 'photos/index.html',context)

def add(request):
    return render (request, 'photos/add.html')    

def view(request,id):
    image = Image.objects.filter(id=id).first()
    
    return render (request, 'photos/view.html',{'image':image})
