from .models import Therapists, TherapySessions, Blogs, BlogComments, TherapistRateScores
from django.contrib import admin


@admin.register(Therapists)
class TherapistsRecords(admin.ModelAdmin):
    list_display = ['name', 'workplace', 'mobile_no', 'county', 'sub_county', 'longitude', 'latitude', 'total_votes']
    readonly_fields = ['name', 'workplace', 'opening_hours', 'closing_hours', 'mobile_no', 'county', 'sub_county', 'longitude', 'latitude', 'total_votes']

@admin.register(TherapySessions)
class TherapySessionsRecords(admin.ModelAdmin):
    list_display = ['therapist', 'patient', 'session_type', 'appointment_date', 'appointment_time', 'booking_date', 'is_approved']
    readonly_fields = ['therapist', 'patient', 'session_type', 'appointment_date', 'appointment_time', 'is_approved']

@admin.register(Blogs)
class BlogsRecords(admin.ModelAdmin):
    list_display = ['blogger', 'total_likes', 'total_comments', 'date_posted']
    readonly_fields = ['blogger', 'blog', 'total_likes', 'total_comments', 'attached_file']

@admin.register(BlogComments)
class BlogCommentsTable(admin.ModelAdmin):
    list_display = ['author', 'date_posted', 'date_edited']
    readonly_fields = ['blog', 'author', 'comment']

@admin.register(TherapistRateScores)
class TherapistRateScores(admin.ModelAdmin):
    list_display = ['therapist', 'rating', 'voting_date']
    readonly_fields = ['therapist', 'rating', 'feedback', 'voting_date', 'date_edited']
