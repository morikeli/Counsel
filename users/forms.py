from .models import Appointments, Facilities
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

