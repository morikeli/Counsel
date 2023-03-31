from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ScheduleAppointmentsForm, AddNewFacilityInfoForm, BlogForm
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import User
from .models import Facilities, Appointments, Testimonials

# views to handle patient requests
@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False and user.is_therapist is False)
def patient_homepage_view(request, patient_name):
    patient_obj = User.objects.get(username=patient_name)
    total_appointments = Appointments.objects.filter(patient=request.user).count()
    total_sessions = Appointments.objects.filter(patient=request.user, is_through=True).count()
    testimonials = Testimonials.objects.all()
    user_sessions = Appointments.objects.filter(patient=request.user, is_through=False)     # used in a table

    context = {
        'total_sessions': total_sessions, 'total_appointments': total_appointments,
        'user_sessions': user_sessions, 'testimonials': testimonials,
    }
    return render(request, 'users/homepage.html', context)


@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False and user.is_therapist is False)
def available_therapists_view(request):
    form = ScheduleAppointmentsForm()

    if request.method == 'POST':
        form = ScheduleAppointmentsForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.name = request.user
            patient.save()

            messages.success(request, 'Appointment schedule successfully!')
            return redirect('schedule_appointment')

    therapists = Facilities.objects.all()
    context = {'ScheduleAppointmentForm': form, 'therapists': therapists, 'total_therapists': therapists.count()}
    return render(request, 'users/therapists.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False and user.is_therapist is False)
def sessions_view(request, name):
    sessions = Appointments.objects.get(patient=request.user)

    context = {'user_sessions': sessions}
    return render(request, 'users/sessions.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False and user.is_therapist is False)
def blogs_view(request):
    testimonials = Testimonials.objects.all()
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()

            messages.success(request, 'Blog uploaded successfully!')
            return redirect('blogs')

    context = {'testimonials': testimonials, 'form': form}
    return render(request, 'users/testimonials.html', context)

# views to handle therapists requests
@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False and user.is_therapist is True and user.therapistprofile.facilities is not None)
def therapists_homepage_view(request, therapist_name):
    therapist_obj = User.objects.get(username=therapist_name)


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

