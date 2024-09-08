
from django.http import HttpResponse
from .models import MyModel
import threading

def create_object(request):
    print(f"View running in thread: {threading.get_ident()}")
    # Creating an instance of MyModel
    obj = MyModel.objects.create(name="Test")
    print("Object created.")
    return HttpResponse("Object created and signal handled.")
