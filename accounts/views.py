from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm, UpdateProfileForm, EditProfileForm
from .models import User


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
                    if user_account.is_therapist is True:
                        auth.login(request, user_account)
                        return redirect('profile')
                    
                    else:
                        auth.login(request, user_account)
                        return redirect('therapist_homepage')
                
                elif user_account.is_staff is False:
                    if  user_account.is_patient is True:
                        auth.login(request, user_account)
                        return redirect('profile')

                    else:
                        auth.login(request, user_account)
                        return redirect('patient_homepage')

            else:
                messages.error(request, 'INVALID CREDENTIALS!!')
                return redirect('user_login')    


    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()

            messages.success(request, f'Account created successfully!')
            return redirect('patient_profile', new_user.username)

    context = {'signup_form': form}
    return render(request, 'patients/signup.html', context)


@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False)
def user_profile_view(request, name):
    user_obj = User.objects.get(username=name)
    updateprofile_form = UpdateProfileForm(instance=user_obj)
    editprofile_form = EditProfileForm(instance=user_obj)

    if request.method == 'POST':
        updateprofile_form = UpdateProfileForm(request.POST, request.FILES, instance=user_obj)
        editprofile_form = EditProfileForm(request.POST, request.FILES, instance=user_obj)

        if updateprofile_form.is_valid():
            new_patient = updateprofile_form.save(commit=False)
            new_patient.is_patient = True
            new_patient.save()

            messages.success(request, 'Your profile was updated successfully!')
            return redirect('profile', name)

        elif editprofile_form.is_valid():
            editprofile_form.save()

            messages.info(request, 'Profile edited successfully!')
            return redirect('profile', name)

    context = {'UpdateProfileForm': updateprofile_form, 'EditProfileForm': editprofile_form}
    return render(request, 'patients/profile.html', context)


class LogoutUserView(LogoutView):
    template_name = 'accounts/logout.html'

