from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.conf import settings
from .forms import SignupForm, EditProfileForm
import os


class UserLoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = ''

        context = {'LoginForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ''

        context = {'LoginForm': form}
        return render(request, self.template_name, context)

class SignupView(SessionWizardView):
    """ This view enables a user to create new account. """
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))
    form_list = [SignupForm, ]
    template_name = 'accounts/signup.html'

    def done(self, form_list, **kwargs):
        registration_form = form_list[1]
        new_user = form_list[0].save(commit=False)
        
        if registration_form.is_valid():
            new_store = registration_form.save(commit=False)
            new_store.owner = new_user
            new_user.save()
            new_store.save()
            
            messages.success(self.request, 'Account successfully created!')
            return redirect('login')

@method_decorator(login_required(login_url='login'), name='get')
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
