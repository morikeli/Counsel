from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ScheduleAppointmentsForm


# views to handle patient requests

def patient_homepage_view(request):

    context = {}
    return render(request, 'users/', context)



def schedule_appointments_view(request):
    form = ScheduleAppointmentsForm()

    if request.method == 'POST':
        form = ScheduleAppointmentsForm(request.POST)
        if form.is_valid():
            patient = forms.save(commit=False)
            patient.name = request.user.patientsprofile
            patient.save()

            message.success(request, 'Appointment schedule successfully!')
            return redirect('')


    context = {'ScheduleAppointmentForm': form}
    return render(request, 'users/', context)

# views to handle therapists requests