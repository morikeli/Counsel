from django.urls import path
from . import views

urlpatterns = [
    path('homepage/patient/', views.patient_homepage_view, name='patient_homepage'),
    path('schedule-appointment/', views.schedule_appointments_view, name='schedule_appointment'),
    
    path('homepage/therapist/', views.therapists_homepage_view, name='therapist_homepage'),
    path('therapist/add-facility-info/', views.update_facility_info_view, name='medical_facility'),

]