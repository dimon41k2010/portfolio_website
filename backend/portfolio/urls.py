from django.urls import path

from . import views

urlpatterns = [
  path('project/', views.get_projects),
  path('project/category', views.get_categories),
  
]