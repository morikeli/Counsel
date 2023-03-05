from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class PatientsProfile(models.Model):
    id = models.CharField(max_length=18, primary_key=True, editable=False, unique=True)
    patient = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    dob = models.DateField(blank=False)
    profile_pic = models.ImageField(upload_to='Patients-Dps/', default='default.png')
    marital_status = models.CharField(max_length=30, blank=False)
    is_patient = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Patients'
        ordering = ['patient']

    def __str__(self):
        return f'{self.patient}'

    def save(self, *args, **kwargs):
        super(PatientsProfile, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)
        if dp.height > 500 and dp.width > 500:
            output_size = (500, 500)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)


class TherapistsProfile(models.Model):
    id  = models.CharField(max_length=18, primary_key=True, unique=True, editable=False)
    counsellor = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    dob = models.DateField(blank=False)
    profile_pic = models.ImageField(upload_to='Counsellors-Dps/', default='default.png')
    marital_status = models.CharField(max_length=30, blank=False)
    is_therapist = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Counsellors'
        ordering = ['counsellor']

    def __str__(self):
        return f'{self.counsellor}'

    def save(self, *args, **kwargs):
        super(CounsellorsProfile, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)
        if dp.height > 500 and dp.width > 500:
            output_size = (500, 500)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)

