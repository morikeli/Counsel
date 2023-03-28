from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .forms import SignupForm
from .models import User


class UsersLayout(UserAdmin):
    model = User
    add_form = SignupForm
    list_display = ['patient', 'gender', 'marital_status', 'is_patient']
    readonly_fields = ['patient', 'gender', 'phone_no', 'dob', 'marital_status', 'is_patient', 'profile_pic']

admin.site.register(User, UsersLayout)