from .forms import (PatientsSignupForm, TherapistsSignupForm, UpdatePatientsProfileForm,
    UpdateTherapistsProfileForm, EditPatientsProfileForm, EditTherapistsProfileForm)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LogoutView
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PatientsProfile, TherapistsProfile


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_account = auth.authenticate(username=username, password=password)
            
            if user_account is not None:
                if user_account.is_staff is True:
                    if user_account.therapistsprofile is True and user_account.therapistsprofile.is_therapist is True:
                        auth.login(request, user_account)
                        return redirect('therapist_profile', user_account.therapistsprofile.medic)
                    
                    else:
                        auth.login(request, user_account)
                        return redirect('therapist_homepage')
                
                elif user_account.is_staff is False:
                    if  user_account.is_staff is False and user_account.patientsprofile.is_patient is False:
                        auth.login(request, user_account)
                        return redirect('patient_profile', user_account.patientsprofile.patient)

                    else:
                        auth.login(request, user_account)
                        return redirect('patient_homepage')

            else:
                messages.error(request, 'INVALID CREDENTIALS!!')
                return redirect('user_login')    


    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def signup_view(request):
    form = PatientsSignupForm()

    if request.method == 'POST':
        form = PatientsSignupForm(request.POST)
        if form.is_valid():
            # this code fetches the name of the patient. The name is used as a parameter when redirecting a user to his/her homepage.
            new_patient_account = form.save(commit=False)
            new_patient_account.save()

            messages.success(request, f'Account created successfully!')
            return redirect('patient_profile', new_patient_account.patientsprofile.patient)

    context = {'signup_form': form}
    return render(request, 'patients/signup.html', context)


def counsellor_signup_view(request):
    form = CounsellorsSignupForm()

    if request.method == 'POST':
        form = CounsellorsSignupForm(request.POST)

        if form.is_valid():
            new_therapist_account = form.save(commit=False)
            new_therapist_account.is_staff = True
            new_therapist_account.save()

            messages.success(request, f'Account for {new_therapist_account.username} created successfully!')
            return redirect('therapist_profile')


    context = {'therapist_signup_form': form}
    return render(request, 'counsellors/counsellors-signup.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False)
def patientsprofile_view(request, patient_name):
    current_patient = PatientsProfile.objects.get(patient__username=patient_name)     # current patient request
    updateprofile_form = UpdatePatientsProfileForm(instance=request.user.patientsprofile)
    editprofile_form = EditPatientsProfileForm(instance=request.user.patientsprofile)

    if request.method == 'POST':
        updateprofile_form = UpdatePatientsProfileForm(request.POST, request.FILES, instance=request.user.patientsprofile)
        editprofile_form = EditPatientsProfileForm(request.POST, request.FILES, instance=request.user.patientsprofile)

        if updateprofile_form.is_valid():
            new_patient = updateprofile_form.save(commit=False)
            new_patient.is_patient = True
            new_patient.save()

            messages.success(request, 'Your profile was updated successfully!')
            return redirect('patient_profile', patient_name)

        elif editprofile_form.is_valid():
            editprofile_form.save()

            messages.info(request, 'Profile edited successfully!')
            return redirect('patient_profile', patient_name)

    context = {'UpdateProfileForm': updateprofile_form, 'EditProfileForm': editprofile_form}
    return render(request, 'patients/profile.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
def therapistprofile_view(request, medic_name):
    current_therapist = TherapistsProfile.objects.get(counsellor__username=medic_name)    # get a logged in therapist request
    updateprofile_form = UpdateTherapistsProfileForm(instance=request.user.therapistsprofile)
    editprofile_form = EditTherapistsProfileForm(instance=request.user.therapistsprofile)

    if request.method == 'POST':
        updateprofile_form = UpdateTherapistsProfileForm(request.POST, request.FILES, instance=request.user.therapistsprofile)
        editprofile_form = EditTherapistsProfileForm(request.POST, request.FILES, instance=request.user.therapistsprofile)

        if updateprofile_form.is_valid():
            new_therapist = updateprofile_form.save(commit=False)
            new_therapist.is_therapist = True
            new_therapist.save()

            messages.success(request, 'Your profile was updated successfully!')
            return redirect('therapist_profile', medic_name)

        elif editprofile_form.is_valid():
            editprofile_form.save()

            messages.info(request, 'Profile edited successfully!')
            return redirect('therapist_profile', medic_name)

    context = {'UpdateProfileForm': updateprofile_form, 'EditProfileForm': editprofile_form}
    return render(request, 'counsellors/profile.html', context)


class LogoutUserView(LogoutView):
    template_name = 'accounts/logout.html'

