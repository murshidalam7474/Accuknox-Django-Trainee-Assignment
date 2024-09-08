from django.shortcuts import render

# Create your views here.
# myapp3/views.py

from django.http import HttpResponse
from .models import MyModel
from django.db import transaction  # Import the transaction module

def create_object(request):
    # Creating an instance of MyModel
    obj = MyModel.objects.create(name="Original")

    # Printing the name of the object before and after saving
    print("Name before save:", obj.name)

    # Start a new transaction explicitly
    with transaction.atomic():
        # Updating the object within the transaction
        obj.name = "Updated"
        obj.save()  # Save the modified object

    # Printing the name of the object after saving
    print("Name after save:", obj.name)

    return HttpResponse("Object created and modified.")
