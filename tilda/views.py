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

# def add(request):
#     categories = Category.objects.all()
#     locations = Location.objects.all()

#     if request.method == 'POST':
#         data = request.POST
#         image = request.FILES.get('image')
    
        

#     context = {
#         'categories': categories,
#         'locations': locations,
#     }
#     return render (request, 'photos/add.html',context)    

def view(request,id):
    image = Image.objects.get(id=id)
    
    return render (request, 'photos/view.html',{'image':image})


def search_results(request):
    query = request.GET.get('query')

    if query:
        searched_images = Image.objects.filter(category__name__icontains=query)
        print(searched_images)
        message = f"{query}"
        

        return render(request, 'photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})

def location(request,id):
    location = Location.objects.get(id=id)
    images = Image.objects.filter(location=location)  
    return render(request, 'photos/location.html',{'images':images})      



        