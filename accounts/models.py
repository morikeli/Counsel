from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    id = models.CharField(max_length=25, primary_key=True, editable=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    dob = models.DateField(blank=False, null=True)
    profile_pic = models.ImageField(upload_to='Patients-Dps/', default='default.png')
    marital_status = models.CharField(max_length=30, blank=False)
    is_patient = models.BooleanField(default=False, editable=False)
    is_therapist = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = 'Patients'
        ordering = ['patient']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)
        if dp.height > 500 and dp.width > 500:
            output_size = (500, 500)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)
