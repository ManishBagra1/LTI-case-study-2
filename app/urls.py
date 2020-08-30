from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='homepage'),
    path('searchstudent/',views.searchstudent,name='search'),
    path('allstudent/',views.displayall,name='Display_all'),
    path('addstudent/',views.addstudent,name="registration")
]