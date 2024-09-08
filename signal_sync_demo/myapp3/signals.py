# myapp3/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

# Define a flag to prevent recursion
processing_signal = False

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    global processing_signal

    # Check if the signal is already being processed
    if processing_signal:
        return

    print("Signal received for:", instance.name)

    # Set the flag to True to indicate that processing is ongoing
    processing_signal = True
    try:
        # Modifying the instance within the signal handler
        instance.name = "Modified"
        instance.save()  # Save the modified instance
    finally:
        # Reset the flag to False after processing
        processing_signal = False
