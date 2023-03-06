from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ScheduleAppointmentsForm, AddNewFacilityInfoForm
from django.shortcuts import render, redirect
from django.contrib import messages


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


def therapists_homepage_view(request):

    context = {}
    return render(request, 'therapists/', context)



def update_facility_info(request):
    form = AddNewFacilityInfoForm()

    if request.method == 'POST':
        form = AddNewFacilityInfoForm(request.POST)
        if form.is_valid():
            new_facility_record = form.save(commit=False)
            new_facility_record.medic = request.user.therapistprofile
            new_facility_record.save()

            messages.success(request, 'Facility has been updated successfully!')
            return redirect('')
            

    context = {}
    return render(request, 'therapists/', context)