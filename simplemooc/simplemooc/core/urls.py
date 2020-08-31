from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contato/', views.contact, name='contato'),
    path('', views.home, name='home'),
]