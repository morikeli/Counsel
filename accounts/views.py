from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.views import View
from django.conf import settings
from .forms import SignupForm, EditProfileForm
from users.forms import TherapistRegistrationForm
import os


class UserLoginView(View):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'LoginForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user_acc = auth.authenticate(username=username, password=password)

            if user_acc is None:    # check if user account exists.
                messages.error(request, 'Invalid credentials! Please try again.')
                return redirect('login')
            
            else:
                if user_acc.is_therapist is False:
                    auth.login(request, user_acc)
                    return redirect('homepage')   # redirect user to patient's homepage
                
                else:
                    auth.login(request, user_acc)
                    return redirect('therapist_dashboard')   # redirect user to therapist homepage

        context = {'LoginForm': form}
        return render(request, self.template_name, context)


def show_therapist_registration_form(wizard):
    """
        This function will display `TherapistRegistrationForm` in the form wizard, if `is_therapist` is True.
    """

    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    is_therapist = cleaned_data.get('is_therapist')
    return is_therapist


class SignupView(SessionWizardView):
    """ This view enables a user to create new account. """

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))
    form_list = [SignupForm, TherapistRegistrationForm]
    template_name = 'accounts/signup.html'
    condition_dict = {
        '1': show_therapist_registration_form,
    }


    def done(self, form_list, **kwargs):
        user_form = form_list[0]

        if user_form.cleaned_data.get('is_therapist') is True:
            user = user_form.save()
            new_therapist = form_list[1].save(commit=False)
            new_therapist.name = user
            new_therapist.save()
        
        else:
            user = user_form.save()
            
        messages.success(self.request, 'Account successfully created!')
        return redirect('login')

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: (user.is_staff is False and user.is_superuser is False)), name='get')
class EditProfileView(View):
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'

    def get(self, request, user, *args, **kwargs):
        form = self.form_class(instance=request.user)

        context = {'EditProfileForm': form,}
        return render(request, self.template_name, context)
    
    def post(self, request, user, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

            messages.info(request, 'Profile successfully updated!')
            return redirect('profile', user)
        
        context = {'EditProfileForm': form,}
        return render(request, self.template_name, context)

class LogoutUser(LogoutView):
    template_name = 'accounts/login.html'
