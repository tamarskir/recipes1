

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index' ),
  
    path('recipe/<int:id>/', views.recipe, name = 'recipe'),
    path('category/<int:id>/', views.category, name = 'category'),
    path('recipe/<int:id>/message/', views.messages, name = 'messages'),
]

