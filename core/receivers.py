from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

from core import models
from django.dispatch import receiver


@receiver(signal=post_save, sender=models.State, dispatch_uid='create_file_state', weak=False)
def create_file_state(instance, **kwargs):
    print(instance)
    with open('states.txt', 'a') as file:
        file.write(f'{instance.pk} - {instance.name}\n')
