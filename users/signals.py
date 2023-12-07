from .models import Therapists, TherapySessions, Blogs, BlogComments, TherapistRateScores
from django.db.models.signals import pre_save
from django import dispatch
import uuid

@dispatch.receiver(pre_save, sender=Therapists)
def generate_therapistsID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:30]

@dispatch.receiver(pre_save, sender=TherapySessions)
def generate_sessionsID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:30]

@dispatch.receiver(pre_save, sender=Blogs)
def generate_blogsID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:30]

@dispatch.receiver(pre_save, sender=BlogComments)
def generate_commentsID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:30]

@dispatch.receiver(pre_save, sender=TherapistRateScores)
def generate_rate_scoresID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:30]
