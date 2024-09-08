# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db import transaction, signals

# class MyModel3(models.Model):
#     name = models.CharField(max_length=100)

# @receiver(post_save, sender=MyModel3)
# def my_signal_handler(sender, instance, **kwargs):
#     print("Signal received for:", instance.name)

#     # Temporarily disconnect the signal to avoid recursion
#     post_save.disconnect(my_signal_handler, sender=MyModel3)
    
#     instance.name = "Modified"
#     instance.save()  # This save will not trigger the signal
    
#     # Reconnect the signal after saving
#     post_save.connect(my_signal_handler, sender=MyModel3)
# from myapp3.models import MyModel3
# from django.db import transaction

# # Create an instance of MyModel3
# obj = MyModel3.objects.create(name="Original")

# # Print name before and after saving
# print("Name before save:", obj.name)  # Will print "Modified" as the signal changes it

# # Explicitly start a new transaction
# with transaction.atomic():
#     obj.name = "Updated"
#     obj.save()

# # Print the final name after the transaction
# print("Name after save:", obj.name)
# myapp3/models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
