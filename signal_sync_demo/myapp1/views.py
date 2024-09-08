# myapp1/views.py

from django.http import HttpResponse
from .models import MyModel

def create_object(request):
    # Creating an instance of MyModel
    obj = MyModel.objects.create(name="Test")
    print("Object created.")
    return HttpResponse("Object created and signal handled.")
