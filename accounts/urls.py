from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user_login'),
    path('create-account/', views.signup_view, name='signup'),
    path('profile/<str:name>/view-profile/', views.user_profile_view, name='patient_profile'),

    path('logout/', views.LogoutUserView.as_view(), name='logout'),

]