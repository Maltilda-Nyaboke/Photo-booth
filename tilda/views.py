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
    categories = Category.objects.all()
    locations = Location.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        print('data:', data) 
        print('image:', data)    

    context = {
        'categories': categories,
        'locations': locations,
    }
    return render (request, 'photos/add.html',context)    

def view(request,id):
    image = Image.objects.get(id=id)
    
    return render (request, 'photos/view.html',{'image':image})
