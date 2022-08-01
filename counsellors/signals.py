from counsellors.models import CounsellorProfile, WorkProfile, LogBook
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from datetime import datetime
import uuid


@receiver(pre_save, sender=CounsellorProfile)
def generate_profile_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).upper().replace("-", "")[:15]


@receiver(post_save, sender=User)
def counsellor_profile_signal(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is True and instance.is_superuser is False:
            CounsellorProfile.objects.create(counsellor=instance)
            WorkProfile.objects.create(name=instance)


@receiver(pre_save, sender=WorkProfile)
def generate_work_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).upper().replace("-", "")[:10]


@receiver(pre_save, sender=LogBook)
def generate_logId(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace("-", "")[:10]


@receiver(pre_save, sender=CounsellorProfile)
def calculate_counsellor_age(sender, instance, **kwargs):
    try:
        if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%m-%d %H:%M:%S'):
            counsellorDob = str(instance.dob)
            strippedDob = datetime.strptime(counsellorDob, '%Y-%m-%d')
            currentDate = datetime.now()
            userAge = currentDate - strippedDob
            calcAge = int(userAge.days/365.25)
            instance.age = calcAge
        
        else:
            counsellorDob = str(instance.dob)
            strippedDob = datetime.strptime(counsellorDob, '%Y-%m-%d')
            currentDate = datetime.now()
            userAge = currentDate - strippedDob
            calcAge = int(userAge.days/365.25)
            instance.age = calcAge
            
    except AttributeError:
        return
    
