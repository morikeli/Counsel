from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .forms import SignupForm
from .models import User


class UsersLayout(UserAdmin):
    model = User
    add_form = SignupForm
    list_display = ['username', 'gender', 'marital_status', 'is_therapist']
    readonly_fields = ['gender', 'phone_no', 'dob', 'marital_status', 'is_therapist', 'profile_pic']

admin.site.register(User, UsersLayout)