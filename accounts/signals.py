from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PatientsProfile, TherapistsProfile
import uuid

@receiver(pre_save, sender=PatientsProfile)
def generate_patientID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]

@receiver(pre_save, sender=TherapistsProfile)
def generate_counsellorID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]

@receiver(post_save, sender=User)
def create_patients_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is False and instance.is_superuser is False:
            PatientsProfile.objects.create(patient=instance)

@receiver(post_save, sender=User)
def create_counsellors_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is True and instance.is_superuser is False:
            TherapistsProfile.objects.create(counsellor=instance)
