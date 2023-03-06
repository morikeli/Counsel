from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user_login'),
    path('create-account/', views.signup_view, name='signup'),
    path('create-staff-account/', views.counsellor_signup_view, name='counsellor_signup'),
    path('profile/<str:patient_name>/view-profile/', views.patientsprofile_view, name='patient_profile'),
    path('profile/<str:medic_name>/therapist/', views.therapistprofile_view, name='therapist_profile'),

    path('logout/', views.LogoutUserView.as_view(), name='logout'),

]