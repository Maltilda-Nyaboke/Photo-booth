from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add.html', views.add, name='add'),
    path('view.html', views.view, name='view')
    
]