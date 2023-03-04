from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user_login'),
    path('create-account/', views.signup_view, name='signup'),
    path('create-staff-account/', views.counsellor_signup_view, name='counsellor_signup'),

]