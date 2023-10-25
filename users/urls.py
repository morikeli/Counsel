from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('session/create/', views.BookTherapySessionsView.as_view(), name='book_session'),
    path('<str:blog_id>/blog/', views.ViewBlogandPostCommentsView.as_view(), name='view_blog_and_comment'),
    
]