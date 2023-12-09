from .forms import ApproveTherapySessionForm, BookTherapySessionForm, WriteBlogForm, WriteBlogCommentsForm, RateTherapistsForm
from .models import Therapists, TherapySessions, Blogs, BlogComments, TherapistRateScores
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: (user.is_staff is False and user.is_superuser is False) or user.is_therapist is False), name='get')
class HomepageView(View):
    """ This is the view responsible for handling a user's homepage requests and responses. """

    form_class_blog = WriteBlogForm
    form_class_comment = WriteBlogCommentsForm
    template_name = 'users/homepage.html'

    def get(self, request, *args, **kwargs):
        blog_form = self.form_class_blog()
        comment_form = self.form_class_comment()

        context = {
            'PostBlogsForm': blog_form,
            'PostCommentsForm': comment_form,

        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        blog_form = self.form_class_blog(request.POST, request.FILES)
        comment_form = self.form_class_comment(request.POST, request.FILES)

        if blog_form.is_valid():
            form = blog_form.save(commit=False)

            form.blogger = request.user
            form.save()

            messages.info(request, 'Blog posted successfully!')
            return redirect('homepage')
        
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.author = request.user
            form.save()

            messages.info(request, 'Comment posted successfully!')
            return redirect('homepage')

        context = {
            'PostBlogsForm': blog_form,
            'PostCommentsForm': comment_form,

        }
        return render(request, self.template_name, context)

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: (user.is_staff is False and user.is_superuser is False) or user.is_therapist is False), name='get')
class ViewBlogandPostCommentsView(View):
    """ This view enables a user to see all comments of a given blog and also post comments related to the blog. """

    form_class = WriteBlogCommentsForm
    template_name = 'users/blog.html'
    
    def get(self, request, blog_id, *args, **kwargs):
        blog = Blogs.objects.get(id=blog_id)
        form = self.form_class()

        context = {
            'PostCommentsForm': form,

        }
        return render(request, self.template_name, context)
    
    def post(self, request, blog_id, *args, **kwargs):
        blog = Blogs.objects.get(id=blog_id)
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blog
            new_comment.author = request.user
            new_comment.save()

            messages.info(request, 'Comment posted successfully!')
            return redirect('view_blog_and_comment')

        context = {
            'PostCommentsForm': form,

        }
        return render(request, self.template_name, context)

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: (user.is_staff is False and user.is_superuser is False) or user.is_therapist is False), name='get')
class TherapistDetailView(View):
    """ This view displays info. about a given therapist and allows the user to book a therapy session with the therapist in addition to rating the therapist. """

    booking_form_class = BookTherapySessionForm
    rating_form_class = RateTherapistsForm
    template_name = 'users/rate.html'

    def get(self, request, therapist_id, *args, **kwargs):
        therapist = Therapists.objects.get(id=therapist_id)
        booking_form = self.booking_form_class()
        rating_form = self.rating_form_class()

        context = {
            'BookTherapySessionForm': booking_form,
            'RateTherapistForm': rating_form,

        }
        return render(request, self.template_name, context)
    
    def post(self, request, therapist_id, *args, **kwargs):
        therapist = Therapists.objects.get(id=therapist_id)
        booking_form = self.booking_form_class(request.POST)
        rating_form = self.rating_form_class(request.POST)

        if booking_form.is_valid():
            new_session = booking_form.save(commit=False)
            new_session.therapist = therapist
            new_session.patient = request.user
            new_session.save()

            messages.info(request, 'Therapy session request submitted successfully!')
            return redirect('therapist_details')
        
        if rating_form.is_valid():
            new_rating_record = rating_form.save(commit=False)
            new_rating_record.therapist = therapist
            new_rating_record.voter = request.user
            new_rating_record.therapist.total_votes += 1
            new_rating_record.save()

            messages.success(request, 'Thanks! Your feedback is highly appreciated!')
            return redirect('therapist_details')

        context = {
            'BookTherapySessionForm': booking_form,
            'RateTherapistForm': rating_form,

        }
        return render(request, self.template_name, context)

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: (user.is_staff is False and user.is_superuser is False) or user.is_therapist is True), name='get')
class DashboardView(View):
    """ This view displays a therapist's dashboard. """

    template_name = 'therapists/homepage.html'

    def get(self, request, therapist, pk, *args, **kwargs):

        context = {

        }
        return render(request, self.template_name, context)
    
    def post(self, request, therapist, pk, *args, **kwargs):

        context = {

        }
        return render(request, self.template_name, context)

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: (user.is_staff is False and user.is_superuser is False) or user.is_therapist is True), name='get')
class ApproveTherapySessionView(View):
    """ This view enables a therapist to approve a booked session. """

    form_class = ApproveTherapySessionForm
    template_name = 'therapists/approve.html'

    def get(self, request, therapy_session, *args, **kwargs):
        booked_session = TherapySessions.objects.get(id=therapy_session)
        form = self.form_class(instance=booked_session)

        context = {
            'ApproveBookedSessionForm': form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, therapy_session, *args, **kwargs):
        booked_session = TherapySessions.objects.get(id=therapy_session)
        form = self.form_class(request.POST, instance=booked_session)

        if form.is_valid():
            form.save()

            messages.success(request, 'Therapy session approved successfully!')
            return redirect('approve_session')

        context = {
            'ApproveBookedSessionForm': form,
        }
        return render(request, self.template_name, context)

