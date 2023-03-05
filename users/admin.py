from .models import Appointments, Facilities
from django.contrib import admin


@admin.register(Appointments)
class FacilitiesTable(admin.ModelAdmin):
    list_display = ['medic', 'facility_name', 'location', 'role', 'opening_hours', 'closing_hours']
    readonly_fields = ['medic', 'facility_name', 'location', 'role', 'mobile_no', 'opening_hours', 'closing_hours']


@admin.register(Facilities)
class AppointmentsTable(admin.ModelAdmin):
    list_display = ['name', 'therapist_name', 'session', 'approved']
    readonly_fields = ['name', 'therapist_name', 'appointment_date', 'appointment_time', 'session', 'approved']

