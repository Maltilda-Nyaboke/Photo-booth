from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('add/', views.add, name='add'),
    path('view/<int:id>', views.view, name='view'),
    path('search_results/',views.search_results, name='search_results'),
    path('location/<int:id>',views.location, name='location'),
    
]