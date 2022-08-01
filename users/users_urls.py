from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('create-useraccount/', views.signup_view, name='signup'),
    path('homepage/', views.homepage_view, name='user_homepage'),
    path('my-profile/', views.userProfile_view, name='user_profile'),
    path('medical-support/', views.medical_support_view, name='medic'),
    path('counselling-session/', views.join_meeting_view, name='meeting'),
    path('your-scheduled-sessions/', views.scheduled_apppointments_view, name='user_sessions'),
    path('help/contact-me/<str:location>/<str:name>/', views.contact_us_view, name='contact_us'),
    path('frequently-asked-questions/', views.faq_view, name='faq'),
    path('testimonials/share-your-experience/', views.testimonials_view, name='testimonials'),
    path('edit-form/<str:pk>/', views.edit_scheduled_appointments_view, name='edit'),
    
    
    path('logged-out/', views.LogoutUser.as_view(), name='logout_user'),
]