from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ScheduleAppointmentsForm, AddNewFacilityInfoForm
from django.shortcuts import render, redirect
from django.contrib import messages


# views to handle patient requests
@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False and user.is_patient is True)
def patient_homepage_view(request):

    context = {}
    return render(request, 'users/homepage.html', context)


@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False and user.is_patient is True)
def schedule_appointments_view(request):
    form = ScheduleAppointmentsForm()

    if request.method == 'POST':
        form = ScheduleAppointmentsForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.name = request.user
            patient.save()

            messages.success(request, 'Appointment schedule successfully!')
            return redirect('schedule_appointment')


    context = {'ScheduleAppointmentForm': form}
    return render(request, 'users/', context)


# views to handle therapists requests
@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False and user.is_therapist is True and user.therapistprofile.facilities is not None)
def therapists_homepage_view(request):

    context = {}
    return render(request, 'therapists/homepage.html', context)


# this view is used by a therapist to add medical facility he/she is employed.
@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False and user.is_therapist is True)
def update_facility_info_view(request):
    form = AddNewFacilityInfoForm()

    if request.method == 'POST':
        form = AddNewFacilityInfoForm(request.POST)
        if form.is_valid():
            new_facility_record = form.save(commit=False)
            new_facility_record.medic = request.user
            new_facility_record.save()

            messages.success(request, 'Facility has been updated successfully!')
            return redirect('medical_facility')
            

    context = {'AddFacilityForm': form}
    return render(request, 'therapists/', context)

