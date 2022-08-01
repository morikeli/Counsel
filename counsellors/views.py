from counsellors.forms import AppointmentForm, SignUpForm, UpdateLogBookForm, UpdateProfileForm, EditProfileForm, UpdateWorkProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from counsellors.models import LogBook
from users.models import UserAppointment, Feedback
from datetime import datetime


def counsellor_login(request):
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            counsellor = auth.authenticate(username=username, password=password)
            
            if counsellor is not None and counsellor.is_staff is True:
                auth.login(request, counsellor)
                return redirect('counsellor_homepage')                
                
            else:
                messages.error(request, 'Please enter a correct name (i.e first name and surname you used to create an account) and password. Note that both fields may be case-sensitive.')
                
            return redirect('counsellor_login')
    
    context = {'form': form}
    return render(request, 'counsellors/login.html', context)
def signup_view(request):
    signup_form = SignUpForm()
    
    if request.method== 'POST':
        signup_form = SignUpForm(request.POST)
        
        if signup_form.is_valid():
            couns = signup_form.save(commit=False)
            couns.is_staff = True
            couns.username = couns.first_name + ' ' + couns.last_name
            couns.save()
                
            messages.success(request, 'You have successfully created a new account!')
            return redirect('counsellor_profile')
    
    context = {'signup_form': signup_form}
    return render(request, 'counsellors/signup.html', context)

@login_required(login_url='counsellor_login')
def homepage_view(request):
    sch_session = UserAppointment.objects.filter(medic=request.user.counsellorprofile.counsellor).all().order_by('scheduled')
    user_feedback = Feedback.objects.filter().all()
    
    context = {'appointments': sch_session, 'user_feedback': user_feedback, 'feedback_count': user_feedback.count(), 
        'total_appointments_today': sch_session.filter(scheduled__contains=datetime.today().strftime("%Y-%m-%d")).count(),
        'total_appointments_month': sch_session.filter(scheduled__contains=datetime.today().strftime("%Y-%m")).count(),
        
    }
    return render(request, 'counsellors/homepage.html', context)


@login_required(login_url='counsellor_login')
def counsellor_profile_view(request):
    update_form = UpdateProfileForm(instance=request.user.counsellorprofile)
    edit_form = EditProfileForm(instance=request.user.counsellorprofile)
    work_form = UpdateWorkProfileForm(instance=request.user.workprofile)
    
    if request.method == 'POST':
        update_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.counsellorprofile)
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.counsellorprofile)
        work_form = UpdateWorkProfileForm(request.POST, instance=request.user.workprofile)
        
        if update_form.is_valid() and work_form.is_valid():
            update_form.save()
            work_form.save()
            messages.success(request, 'Profile updated successfully!')
            
        elif edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Profile edited successfully!')
            
        return redirect('counsellor_profile')
    
    context = {'updateprofile_form': update_form, 'editprofile_form': edit_form, 'workprofile_form': work_form}
    return render(request, 'counsellors/profile.html', context)


@login_required(login_url='counsellor_login')
def appointments_view(request):
    sch_session = UserAppointment.objects.filter(medic=request.user.counsellorprofile.counsellor).all().order_by('scheduled')
    
    context = {'sessions': sch_session}
    return render(request, 'counsellors/sessions.html', context)

@login_required(login_url='counsellor_login')
def advise_view(request):
    
    context = {}
    return render(request, 'counsellors/advice.html', context)


@login_required(login_url='counsellor_login')
def approve_appointment_view(request, schedule):
    obj = UserAppointment.objects.get(scheduled=schedule)
    approval_form = AppointmentForm(instance=obj)
    
    if request.method == 'POST':
        approval_form = AppointmentForm(request.POST, instance=obj)

        if approval_form.is_valid():
            approval_form.save()
            
            messages.success(request, 'You have approved this appointment')
            return redirect('counsellor_sessions')
    
    context = {'obj': obj, 'approval_form': approval_form}
    return render(request, 'counsellors/approve.html', context)


@login_required(login_url='counsellor_login')
def log_book_view(request):       
    logs = LogBook.objects.filter(log_name=request.user.counsellorprofile)
    
    log_form = UpdateLogBookForm()
    if request.method == 'POST':
        log_form = UpdateLogBookForm(request.POST)
        
        if log_form.is_valid():
            log = log_form.save(commit=False)
            log.log_name = request.user.counsellorprofile
            log.save()
            
            messages.success(request, "Today's log book has been updated successfully!")
            return redirect('log_book')
        
    context = {
        'log_form': log_form, 'log_book': logs,
        'current_date': logs.filter(created__date__contains=datetime.today().strftime("%Y-%m-%d")).exists(),

    }
    return render(request, 'counsellors/log-book.html', context)


@login_required(login_url='counsellor_login')
def edit_logbook_view(request, pk):
    obj = LogBook.objects.get(created=pk)
    edit_form = UpdateLogBookForm(instance=obj)
    
    if request.method == 'POST':
        edit_form = UpdateLogBookForm(request.POST, instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            
            messages.info(request, 'Log edited successfully!')
            return redirect('log_book')
        
    context = {'edit_form': edit_form}
    return render(request, 'counsellors/edit-log.html', context)


class LogoutUser(LogoutView):
    template_name = 'counsellors/logout.html'