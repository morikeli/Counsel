from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientsSignupForm, CounsellorsSignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LogoutView


@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
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


@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False)
def signup_view(request):
    form = PatientsSignupForm()

    if request.method == 'POST':
        form = PatientsSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()

            messages.success(request, f'Account {new_user.username} created successfully!')
            return redirect('user_login')

    context = {'signup_form': form}
    return render(request, 'accounts/signup.html', context)


@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False)
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
    return render(request, 'accounts/counsellors-signup.html', context)

@user_passes_test(lambda user: user.is_authenticated is False)
class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

