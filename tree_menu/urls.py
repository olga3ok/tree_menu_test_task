from django.contrib import admin
from django.urls import path
from .views import index


urlpatterns = [
    path('', index),
    path('<int:item_id>/', index, name='index')
]
