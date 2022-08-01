from django.contrib.auth.forms import UserCreationForm
from counsellors.models import CounsellorProfile, LogBook, WorkProfile
from users.models import UserAppointment
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
class UpdateProfileForm(forms.ModelForm):
    choice_gender = (
        (None, '-- select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    choice_marital = (
        (None, '-- marital status --'),
        ('Dating', 'Dating'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married')
    )
    
    dp = forms.ImageField(widget=forms.FileInput(), label='Profile picture')
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='', help_text='Enter your date of birth')
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2 mb-2'}), label='', choices=choice_gender)
    location = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2 mb-2', 'placeholder': 'Enter location/country of origin'}), label='')
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2', 'placeholder': 'Enter your mobile no.'}), label='')
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), label='', choices=choice_marital)
    
    class Meta:
        model = CounsellorProfile
        fields = ['dp', 'gender', 'dob', 'location', 'phone_no', 'marital_status']

class EditProfileForm(forms.ModelForm):
    choice_marital = (
        (None, '-- marital status --'),
        ('Dating', 'Dating'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married')
    )
    
    dp = forms.ImageField(widget=forms.FileInput(), label='Profile picture')
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=choice_marital)
    
    class Meta:
        model = CounsellorProfile
        fields = ['dp', 'phone_no', 'marital_status']


class UpdateWorkProfileForm(forms.ModelForm):
    org = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Where do you work?', 'class': 'mb-2'}), label='', help_text='')
    location = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter location of your place of work ...', 'class': 'mb-2'}), label='', help_text='', required=True)
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel',  'class': 'mt-2', 'placeholder': 'Enter mobile no.'}), label='', help_text='Enter mobile no. others can call to reach you')
    role = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'What is your role?'}), label='', help_text='Mention if you are a counsellor, psychologist, etc.')
    opening_hours = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time',  'class': 'mt-2'}), label='', help_text='Opening hours')
    closing_hours = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time',  'class': 'mt-3'}), label='', help_text='Closing hours')
    
    class Meta:
        model = WorkProfile
        fields = ['org', 'location', 'role', 'mobile_no', 'opening_hours', 'closing_hours']


class AppointmentForm(forms.ModelForm):
    choice_session = (
        (None, '-- choose session -- '),
        ('Physical', 'Physical'),
        ('Virtual', 'Virtual')
    )
    choice_duration = (
        (None, '-- select timeline -- '),
        ('Began Recently', 'Began Recently'),
        ('1 week', '1 week'),
        ('2 weeks', '2 weeks'),
        ('3 weeks', '3 weeks'),
        ('Month', 'Month'),
        ('More than a month', 'More than a month'),
        ('More than a year', 'More than a year'),
    )
    choice_approval = (
        (None, '-- select choice --'),
        ('Approve', 'Approve'),
    )
    
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mt-2'}), help_text='Appointment time', label='', disabled=True)
    type_session = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), label='', choices=choice_session, disabled=True)
    duration = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2'}), choices=choice_duration, help_text='This user says this has been happening for the stated period of time stated above', label='', disabled=True)
    approval = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mt-3'}), label='', choices=choice_approval, help_text='do you wish to approve this meeting?')
    
    class Meta:
        model = UserAppointment
        fields = ['appointment_time', 'type_session', 'duration', 'approval']


class UpdateLogBookForm(forms.ModelForm):
    patient = forms.CharField(widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Enter the name of the patient you counselled....', 'class': 'mt-2'}), label='', required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Describe the session....', 'class': 'mt-2'}), label='', required=True, help_text='Describe the counselling session in details')
    
    class Meta:
        model = LogBook
        fields = ['patient', 'description']