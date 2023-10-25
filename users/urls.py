from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('details/<str:therapist_id>/therapist/', views.TherapistDetailView.as_view(), name='therapist_details'),
    path('<str:blog_id>/blog/', views.ViewBlogandPostCommentsView.as_view(), name='view_blog_and_comment'),
    path('session/<str:therapy_session>/approve/', views.ApproveTherapySessionView.as_view(), name='approve_session'),
    
]