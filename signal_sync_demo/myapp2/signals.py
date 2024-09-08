
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import threading
import time

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    print(f"Signal handler running in thread: {threading.get_ident()}")
    time.sleep(2)  # Simulate some delay in the signal handler
    print("Signal handler execution completed.")
