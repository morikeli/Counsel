from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PatientsProfile, TherapistsProfile
from django import forms

# custom forms for patients
class PatientsSignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UpdatePatientsProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced')
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_MARITAL_STATUS, required=True)

    class Meta:
        model = PatientsProfile
        fields = ['dob', 'gender', 'phone_no', 'marital_status', 'profile_pic']

class EditPatientsProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced')
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), disabled=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, disabled=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_MARITAL_STATUS, required=True)

    class Meta:
        model = PatientsProfile
        fields = ['dob', 'gender', 'phone_no', 'marital_status', 'profile_pic']


# custom made forms for counsellors
class TherapistsSignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']



class UpdateTherapistsProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced')
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_MARITAL_STATUS, required=True)

    class Meta:
        model = TherapistsProfile
        fields = ['dob', 'gender', 'phone_no', 'marital_status', 'profile_pic']

class EditTherapistsProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced')
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), disabled=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, disabled=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_MARITAL_STATUS, required=True)

    class Meta:
        model = TherapistsProfile
        fields = ['dob', 'gender', 'phone_no', 'marital_status', 'profile_pic']
