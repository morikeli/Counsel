from django.urls import path
from . import views

urlpatterns = [
    path('homepage/<str:patient_name>/', views.patient_homepage_view, name='patient_homepage'),
    path('schedule-appointment/', views.available_therapists_view, name='therapists'),
    path('<str:name>/sessions', views.sessions_view, name='sessions'),
    path('blogs/', views.blogs_view, name='blogs'),
    
    path('homepage/<str:therapist_name>/', views.therapists_homepage_view, name='therapist_homepage'),
    path('therapist/add-facility-info/', views.update_facility_info_view, name='medical_facility'),

]