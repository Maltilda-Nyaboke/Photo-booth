from multiprocessing import context
from django.shortcuts import render,redirect
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
    
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        else:
            category = None
            
        image = Image.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )


        if data['location'] != 'none':
            location = Location.objects.get(id=data['location'])
        else:
            location = None 
        image = Image.objects.create(
            location=location,
            description=data['description'],
            image=image,
        )   
        return redirect('home')
    context = {
        'categories': categories,
        'locations': locations,
    }
    return render (request, 'photos/add.html',context)    

def view(request,id):
    image = Image.objects.get(id=id)
    
    return render (request, 'photos/view.html',{'image':image})


def search_image(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})    
