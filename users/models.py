from django.db import models
from django.contrib.auth.models import User
from accounts.models import PatientsProfile, TherapistsProfile


class Appointments(models.Model):
    id = models.CharField(max_length=20, primary_key=True, editable=False, unique=True)
    name = models.ForeignKey(PatientsProfile, on_delete=models.CASCADE,editable=False)
    therapist_name = models.CharField(max_length=100, blank=False)
    appointment_date = models.DateField(blank=False)
    appointment_time = models.TimeField(blank=False)
    session = models.CharField(max_length=20, blank=False)
    approved = models.BooleanField(default=False, editable=False)
    scheduled = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Appointments'
        ordering = ['-scheduled']

    def __str__(self):
        return f'{self.name}'


class Facilities(models.Model):
    id = models.CharField(max_length=20, primary_key=True, editable=False, unique=True)
    medic = models.OneToOneField(TherapistsProfile, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, blank=False)
    facility_name = models.CharField(max_length=70, blank=False)
    location = models.CharField(max_length=70, blank=False)
    mobile_no = models.CharField(max_length=14, blank=False)
    opening_hours = models.TimeField(blank=False)
    closing_hours = models.TimeField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Facilities'
        ordering = ['facility_name']

    def __str__(self):
        return f'{self.medic}'

