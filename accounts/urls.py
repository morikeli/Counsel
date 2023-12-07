from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('create-account/', views.SignupView.as_view(), name='signup'),
    path('<str:user>/profile/', views.EditProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
]