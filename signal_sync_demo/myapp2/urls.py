# myapp2/urls.py

from django.urls import path
from .views import create_object

urlpatterns = [
    path('create/', create_object, name='create_object'),
]
