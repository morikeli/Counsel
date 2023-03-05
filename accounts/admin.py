from .models import PatientsProfile, TherapistsProfile
from django.contrib import admin


@admin.register(PatientsProfile)
class PatientsTable(admin.ModelAdmin):
    list_display = ['patient', 'gender', 'marital_status', 'is_patient']
    readonly_fields = ['patient', 'gender', 'phone_no', 'dob', 'marital_status', 'is_patient', 'profile_pic']


@admin.register(TherapistsProfile)
class TherapistsTable(admin.ModelAdmin):
    list_display = ['therapist', 'gender', 'marital_status', 'is_therapist']
    readonly_fields = ['therapist', 'gender', 'phone_no', 'dob', 'marital_status', 'is_therapist', 'profile_pic']