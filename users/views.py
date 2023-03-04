from users.forms import (
        FeedbackForm, HelpForm, LoginForm, SignUpForm, UpdateProfileForm, 
        EditProfileForm, ShareExperienceForm, ScheduleAppointmentForm,
                    )
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from counsellors.models import CounsellorProfile, WorkProfile
from users.models import UserAppointment, UserProfile, YourStory
from datetime import datetime


class UserLogin(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'
    

def signup_view(request):
    signupForm = SignUpForm()
    
    if request.method == 'POST':
        signupForm = SignUpForm(request.POST)
        
        if signupForm.is_valid():
            reguser = signupForm.save(commit=False)
            reguser.username = reguser.first_name + ' ' + reguser.last_name
            reguser.is_staff = False
            reguser.save()

            messages.success(request, 'Account created successfully')
            return redirect('user_profile')
        
    context = {'signup_form': signupForm} 
    return render(request, 'users/signup.html', context)

@login_required(login_url='user_login')
def userProfile_view(request):
    update_form = UpdateProfileForm(instance=request.user.userprofile)
    edit_form = EditProfileForm(instance=request.user.userprofile)
    
    if request.method == 'POST':
        update_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        edit_form = EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if update_form.is_valid():
            update_form.save()
            messages.info(request, 'Profile updated successfully!')
        
        elif edit_form.is_valid():
            edit_form.save()
            messages.info(request, 'Profile edited successfully!')
        
        return redirect('user_profile')
    
    context = {'update_form': update_form, 'edit_form': edit_form}
    return render(request, 'users/profile.html', context)


@login_required(login_url='user_login')
def homepage_view(request):
    scheduled_sessions = UserAppointment.objects.filter(patient=request.user.userprofile).all()
    testimonials = YourStory.objects.filter(victim__location__contains=request.user.userprofile.location).all()
    
    calcPrevious_day = int(datetime.now().strftime("%d")) - 1
    previous_day = str(datetime.today().strftime("%Y-%m")) + '-' + str(calcPrevious_day)
    previous_day_sessions = UserAppointment.objects.filter(scheduled__date__contains=previous_day).count()
    today_sessions = UserAppointment.objects.filter(scheduled__date__contains=datetime.today().strftime("%Y-%m-%d")).count()
    percentage_today = (today_sessions - previous_day_sessions)/100
    
    calcPrevious_month = int(datetime.now().strftime("%m")) - 1
    previous_month = str(datetime.today().strftime("%Y")) + '-' + str(calcPrevious_month)
    previous_month_sessions = UserAppointment.objects.filter(scheduled__date__contains=previous_month).count()
    current_month_sessions = UserAppointment.objects.filter(scheduled__date__contains=datetime.today().strftime("%Y-%m-%d")).count()
    percentage_month = (current_month_sessions - previous_month_sessions)/100
    
    qs = UserAppointment.objects.get_queryset().filter(patient=request.user.userprofile)
    print(qs)
    
    
    context = {
        'appointments': scheduled_sessions, 'testimonials': testimonials,
        'total_sessions_today': scheduled_sessions.filter(scheduled=datetime.today()).count(), 
        'total_sessions_monthly': scheduled_sessions.filter(scheduled__date__contains=datetime.today().strftime("%Y-%m")).count(),
        'percent': percentage_today, 'monthly_percent': percentage_month,
        'qs': qs.count(),
    }
    return render(request, 'users/homepage.html', context)


@login_required(login_url='user_login')
def medical_support_view(request):
    med_form = ScheduleAppointmentForm()
    
    if request.method == 'POST':
        med_form = ScheduleAppointmentForm(request.POST)
        if med_form.is_valid():
            med = med_form.save(commit=False)
            
            filter_counsellor_name = UserAppointment.objects.filter(medic=med.medic)
            if filter_counsellor_name.exists() is False:
                messages.error(request, f'Counsellor "{med.medic}" does not exist! Please enter correct name.')
            else:
                filter_schedules = UserAppointment.objects.filter(medic=med.medic, appointment_date=med.appointment_date, appointment_time=med.appointment_time).exists()
                if filter_schedules is True:
                    messages.warning(request, f'{med.medic} has a scheduled appointment at the provided date & time. Kindly reschedule.')
                else:
                    med.patient = request.user.userprofile
                    med.save()
                    messages.success(request, 'Appointment submitted successfully!')
                    return redirect('medic')
    
    my_counsellors = WorkProfile.objects.filter(location__contains=request.user.userprofile.location).order_by('location')
    context = {'schedule_form': med_form, 'counsellors': my_counsellors}
    return render(request, 'users/medical-support.html', context)


@login_required(login_url='user_login')
def join_meeting_view(request):
    progress_form = FeedbackForm()
    get_schedule = UserAppointment.objects.filter().all().order_by('-scheduled')
    
    if request.method == 'POST':
        progress_form = FeedbackForm(request.POST)
        
        if progress_form.is_valid():
            feed = progress_form.save(commit=False)
            feed.name = request.user.userprofile
            
            filter_appointments = UserAppointment.objects.filter(patient=request.user.userprofile).all()
            if filter_appointments is None:
                messages.error(request, 'You have no record of scheduled appointments. Have you been counselled before?')
            
            else:
                filter_counsellor = WorkProfile.objects.filter(name__username__contains=feed.counsellor).values('name').exists()
                if filter_counsellor is False:
                    messages.warning(request, 'INVALID NAME! Please provide correct counsellor\'s name. Name may be case sensitive.')
                    
                else:
                    get_schedule = UserAppointment.objects.filter().all().order_by('-scheduled')
                    get_first_date = [d.scheduled.strftime("%Y-%m-%d %H:%M") for d in get_schedule][0]
                    strip_first_date = datetime.strptime(get_first_date, "%Y-%m-%d %H:%M")
                    total_days = datetime.now() - strip_first_date
                    timeline = int(total_days.days)
                        
                    if timeline <= 30:
                        day_gte = UserAppointment.objects.filter(scheduled__gte=get_first_date).values('medic', 'appointment_date', 'appointment_time')
                        day_lte = UserAppointment.objects.filter(scheduled__lte=datetime.now().strftime("%Y-%m-%d %H:%M")).values('medic', 'appointment_date', 'appointment_time')
                        
                        if day_gte.exists() and day_lte.exists():
                            feed.save()    
                            messages.success(request, 'Your feedback has been submitted successfully!')
                            return redirect('meeting')
                        else:
                            messages.warning(request, 'Have you had any counselling session recently? There are no records found.')
    
    context = {'progress_form': progress_form}
    return render(request, 'users/meeting.html', context)


@login_required(login_url='user_login')
def scheduled_apppointments_view(request):
    user_scheduled_sessions = UserAppointment.objects.filter(patient=request.user.userprofile).order_by('scheduled')
    
    context = {'sessions': user_scheduled_sessions}
    return render(request, 'users/sessions.html', context)


@login_required(login_url='user_login')
def edit_scheduled_appointments_view(request, pk):
    obj = UserAppointment.objects.get(scheduled=pk)
    form = ScheduleAppointmentForm(instance=obj)
    
    if request.method == 'POST':
        form = ScheduleAppointmentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.info(request, 'Appointment edited successfully.')
    
    
    context = {'edit_form': form, 'obj': obj, 'preview': ScheduleAppointmentForm(instance=obj)}
    return render(request, 'users/edit.html', context)


@login_required(login_url='user_login')
def contact_us_view(request, name, location):
    medic_info = User.objects.get(username=name)
    location = medic_info.workprofile.location
    
    context = {'med': medic_info}
    return render(request, 'users/contact-us.html', context)


@login_required(login_url='user_login')
def testimonials_view(request):
    form = ShareExperienceForm()
    if request.method == 'POST':
        form = ShareExperienceForm(request.POST)
        
        if form.is_valid():
            share = form.save(commit=False)
            share.victim = request.user.userprofile
            share.save()
            
            messages.success(request, 'Your story was submitted successfully!')
            return redirect('testimonials')
    
    
    testimonials = YourStory.objects.filter(victim__location__contains=request.user.userprofile.location).all()
    context = {'form': form, 'testimonials': testimonials}
    return render(request, 'users/testimonials.html', context)

@login_required(login_url='user_login')
def faq_view(request):
    quiz_form = HelpForm()
    if request.method == 'POST':
        quiz_form = HelpForm(request.POST)
        if quiz_form.is_valid():
            qf = quiz_form.save(commit=False)
            qf.questioner = request.user.userprofile
            qf.save()
            
            messages.success(request, 'Question submitted successfully!')
            return redirect('faq')
    
    context = {'faq_form': quiz_form}
    return render(request, 'users/faq.html', context)


class LogoutUser(LogoutView):
    template_name = 'users/logout.html'
    