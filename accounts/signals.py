from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import User
from datetime import datetime
import uuid

@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]
    
    try:
        if instance.is_superuser is True:
            pass    # dob is not required for superuser account, thus leave the 'dob' in user model blank when creating superuser a/c.
        else:
            if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.created.strftime('%Y-%m-%d %H:%M:%S'):
                user_dob = str(instance.dob)
                get_userDob = datetime.strptime(user_dob, '%Y-%m-%d')
                current_date = datetime.now()
                user_age = current_date - get_userDob
                convert_userAge = int(user_age.days/365.25)
                instance.age = convert_userAge
                
            else:
                user_dob = str(instance.dob)
                get_userDob = datetime.strptime(user_dob, '%Y-%m-%d')
                current_date = datetime.now()
                user_age = current_date - get_userDob
                convert_userAge = int(user_age.days/365.25)
                instance.age = convert_userAge
            
    except AttributeError:
        return
