from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from .models import User
from uuid import uuid4


@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:30]

    try:
        # Calculate a user's age
        if instance.is_superuser is False:
            if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.date_joined.strftime('%Y-%m-%d %H:%M:%S'):
                user_dob = instance.dob
                current_date = datetime.now().date()
                age = current_date - user_dob
                instance.age = int(age.days/365.25)
                
            else:
                user_dob = instance.dob
                current_date = datetime.now().date()
                age = current_date - user_dob
                instance.age = int(age.days/365.25)
    
    except AttributeError:
        return