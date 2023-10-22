from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=30, unique=True, editable=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=7, blank=False)
    mobile_no = PhoneNumberField(blank=False)
    age = models.PositiveSmallIntegerField(default=0, editable=False)
    dob = models.DateField(null=True, blank=False)
    marital_status = models.CharField(max_length=10, blank=False)
    profile_pic = models.ImageField(upload_to='Users/dps/', default='default.png')
    is_therapist = models.BooleanField(default=False)
    date_edited = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.username
    
    def save(self, *args, **kwargs):
        super(self, User).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)
        
        if img.height >= 320 and img.width >= 320:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
        