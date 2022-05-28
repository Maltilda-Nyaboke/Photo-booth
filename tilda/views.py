from django.shortcuts import render


# Create your views here.
def home(request):
    return render (request, 'photos/index.html')

def add(request):
    return render (request, 'photos/add.html')    

def view(request):
    return render (request, 'photos/view.html')
