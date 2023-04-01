from .models import Appointments, Facilities, Testimonials
from django import forms

class ScheduleAppointmentsForm(forms.ModelForm):
    # try using a qs to select all therapists in a select field
    SELECT_THERAPISTS = (
        (None, '-- Select therapist --'),

    )
    SELECT_SESSION = (
        (None, '-- Select type of session --'),
        ('Physical Session', 'Physical Session'),
        ('Virtual session', 'Virtual Session'),
    )

    therapist_name = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_THERAPISTS, required=True)
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), required=True)
    appointment_date = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mb-2'}), required=True)
    session = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_SESSION, required=True)
    class Meta:
        model = Appointments
        fields = ['therapist_name', 'appointment_date', 'appointment_time', 'session']


class AddNewFacilityInfoForm(forms.ModelForm):
    SELECT_ROLE = (
        (None, '-- Select role --'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Therapist', 'Therapist')
    )

    role = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_ROLE, required=True)
    facility_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), required=True)
    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), 
        help_text='Enter state/county and country where the facility is located, e.g. Dallas, Texas; Nairobi, Kenya', required=True)
    opening_hours = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mb-2'}), required=True)
    closing_hours = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mb-2'}), 
        help_text='Enter time in 24-hour clock format', required=True)
    mobile_no = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), 
        help_text='Enter your office mobile number', required=True)

    class Meta:
        model = Facilities
        fields = ['role', 'facility_name', 'location', 'opening_hours', 'closing_hours', 'mobile_no']


class BlogForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), label='Blog', help_text='Share your experiences or thoughts')

    class Meta:
        model = Testimonials
        fields = ['message']