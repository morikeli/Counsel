from django.urls import path
from counsellors import views

urlpatterns = [
    path('counsellor-login/', views.counsellor_login, name='counsellor_login'),
    path('create-account/', views.signup_view, name='counsellor_signup'),
    path('homepage/', views.homepage_view, name='counsellor_homepage'),
    path('my_profile/counsellor/', views.counsellor_profile_view, name='counsellor_profile'),
    path('log-book/', views.log_book_view, name='log_book'),
    path('counsellor-log-book/edit/<str:pk>/log-book', views.edit_logbook_view, name='edit_log'),
    path('appointments/', views.appointments_view, name='counsellor_sessions'),
    path('approve/<str:schedule>/', views.approve_appointment_view, name='approve'),
    
    
    path('goodbye/counsellor/', views.LogoutUser.as_view(), name='counsellor_logout'),
]