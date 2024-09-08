# myapp1/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    # Simulate some processing delay
    print("Signal handler execution completed.")
