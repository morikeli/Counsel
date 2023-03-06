from django.urls import path
from . import views

urlpatterns = [
    path('homepage/patient/', views.patient_homepage_view, name='patient_homepage'),
    path('schedule-appointment/', views.schedule_appointments_view, name=''),

]