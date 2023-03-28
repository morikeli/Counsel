from .models import Appointments, Facilities
from django.contrib import admin


@admin.register(Facilities)
class FacilitiesTable(admin.ModelAdmin):
    list_display = ['therapist', 'facility_name', 'location', 'role', 'opening_hours', 'closing_hours']
    readonly_fields = [ 'facility_name', 'location', 'role', 'mobile_no', 'opening_hours', 'closing_hours']


@admin.register(Appointments)
class AppointmentsTable(admin.ModelAdmin):
    list_display = ['name', 'therapist_name', 'session', 'approved']
    readonly_fields = ['name', 'therapist_name', 'appointment_date', 'appointment_time', 'session', 'approved']

