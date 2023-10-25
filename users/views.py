from .forms import BookTherapySessionForm, WriteBlogForm, WriteBlogCommentsForm, RateTherapistsForm
from .models import TherapySessions, Blogs, BlogComments, TherapistRateScores
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(lambda user: (user.is_staff is False and user.is_superuser is False and user.is_active is True) or user.is_therapist is False)
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
@method_decorator(lambda user: (user.is_staff is False and user.is_superuser is False and user.is_active is True) or user.is_therapist is False)
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
    