from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Facilities, Appointments
import uuid

@receiver(pre_save, sender=Facilities)
def generate_facilitiesID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "").upper()[:20]

@receiver(pre_save, sender=Appointments)
def generate_appointmentsID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "").upper()[:20]
