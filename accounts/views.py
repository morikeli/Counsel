from .forms import (PatientsSignupForm, CounsellorsSignupForm, UpdatePatientsProfileForm,
    UpdateCounsellorsProfileForm, EditPatientsProfileForm, EditCounsellorsProfileForm)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PatientsProfile, CounsellorsProfile


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
                    if user_account.counsellorsprofile is True:
                        auth.login(request, user_account)
                        return redirect('counsellors_homepage')
                    
                    else:
                        auth.login(request, user_account)
                        return redirect('counsellors_profile')
                
                elif user_account.is_staff is False:
                    if  user_account.is_staff is False:
                        auth.login(request, user_account)
                        return redirect('patient_homepage')

                    else:
                        auth.login(request, user_account)
                        return redirect('patient_profile')

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
            new_user = form.save(commit=False)
            new_user.is_patient = True
            new_user.save()

            messages.success(request, f'Account {new_user.username} created successfully!')
            return redirect('user_login')

    context = {'signup_form': form}
    return render(request, 'patients/signup.html', context)


def counsellor_signup_view(request):
    form = CounsellorsSignupForm()

    if request.method == 'POST':
        form = CounsellorsSignupForm(request.POST)

        if form.is_valid():
            new_counsellor = form.save(commit=False)
            new_counsellor.save()

            messages.success(request, f'Account for {new_counsellor.username} created successfully!')
            return redirect('user_login')


    context = {'counsellor_signup_form': form}
    return render(request, 'counsellors/counsellors-signup.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False and user.patientsprofile.is_patient is True)
def updatepatientsprofile_view(request, patient_name):
    current_patient = PatientsProfile.objects.get(patient=patient_name)
    updateprofile_form = UpdatePatientsProfileForm(instance=request.user.patientsprofile)
    editprofile_form = EditPatientsProfileForm(instance=request.user.patientsprofile)

    if request.method == 'POST':
        updateprofile_form = UpdatePatientsProfileForm(request.POST, request.FILES, instance=request.user.patientsprofile)
        editprofile_form = EditPatientsProfileForm(request.POST, request.FILES, instance=request.user.patientsprofile)

        if updateprofile_form.is_valid():
            updateprofile_form.save()

            messages.success(request, 'Your profile was updated successfully!')
            return redirect('patients_profile', patient_name)

        elif editprofile_form.is_valid():
            editprofile_form.save()

            messages.info(request, 'Profile edited successfully!')
            return redirect('patients_profile', patient_name)

    context = {'UpdateProfileForm': updateprofile_form, 'EditProfileForm': editprofile_form}
    return render(request, 'patients/profile.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False and user.counsellorsprofile.is_counsellor is True)
def updatecounsellorsprofile_view(request, medic_name):
    current_patient = CounsellorsProfile.objects.get(counsellor=medic_name)
    updateprofile_form = UpdateCounsellorsProfileForm(instance=request.user.counsellorsprofile)
    editprofile_form = EditCounsellorsProfileForm(instance=request.user.counsellorsprofile)

    if request.method == 'POST':
        updateprofile_form = UpdatePatientsProfileForm(request.POST, request.FILES, instance=request.user.counsellorsprofile)
        editprofile_form = EditPatientsProfileForm(request.POST, request.FILES, instance=request.user.counsellorsprofile)

        if updateprofile_form.is_valid():
            updateprofile_form.save()

            messages.success(request, 'Your profile was updated successfully!')
            return redirect('patients_profile', patient_name)

        elif editprofile_form.is_valid():
            editprofile_form.save()

            messages.info(request, 'Profile edited successfully!')
            return redirect('patients_profile', patient_name)

    context = {'UpdateProfileForm': updateprofile_form, 'EditProfileForm': editprofile_form}
    return render(request, 'counsellors/profile.html', context)


class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

