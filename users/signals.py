from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from accounts.models import PatientsProfile, CounsellorsProfile
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

@receiver(post_save, sender=CounsellorsProfile)
def save_scheduled_appointments(sender, created, instance, **kwargs):
    if created:
        Facilities.objects.create(name=instance)

@receiver(post_save, sender=PatientsProfile)
def save_scheduled_appointments(sender, created, instance, **kwargs):
    if created:
        Appointments.objects.create(name=instance)
