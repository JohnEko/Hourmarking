from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('create_view/', views.create_view, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete_view/<str:user>/', views.delete_view, name='delete'),
    
]
