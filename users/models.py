from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import User
from django.db import models

class Therapists(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    workplace = models.CharField(max_length=70, blank=False)
    mobile_no = PhoneNumberField(blank=False)
    county = models.CharField(max_length=50, blank=False)
    sub_county = models.CharField(max_length=70, blank=False)
    opening_hours = models.TimeField(blank=False, null=False)
    closing_hours = models.TimeField(blank=False, null=False)
    total_votes = models.PositiveIntegerField(default=0, editable=False)
    longitude = models.FloatField(blank=False, editable=False, default=0)
    latitude = models.FloatField(blank=False, editable=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str or None:
        return self.name
    
    class Meta:
        ordering = ['therapist', 'workplace']
        verbose_name_plural = 'Therapists'
    
class TherapySessions(models.Model):
    id = models.CharField(max_length=30, primary_key=True, editable=False, unique=True)
    therapist = models.ForeignKey(Therapists, on_delete=models.CASCADE, editable=False)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    session_type = models.CharField(max_length=20, blank=False)
    appointment_date = models.DateField(blank=False, null=False)
    appointment_time = models.TimeField(blank=False, null=False)
    is_approved = models.BooleanField(default=False, editable=False)
    booking_date = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str or None:
        return self.therapist
    
    class Meta:
        ordering = ['therapist', 'patient', 'appointment_date', 'appointment_time']
        verbose_name_plural = 'Therapy sessions records'

class Blogs(models.Model):
    id = models.CharField(max_length=30, primary_key=True, editable=False, unique=True)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    blog = models.TextField(blank=False)
    attached_file = models.FileField(upload_to='Blogs/Posts/file-uploads', blank=True)
    total_likes = models.PositiveIntegerField(default=0, editable=False)
    total_comments = models.PositiveIntegerField(default=0, editable=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.blogger
    
    class Meta:
        ordering = ['blogger', 'date_posted']
        verbose_name_plural = 'Testimonials'

class BlogComments(models.Model):
    id = models.CharField(max_length=30, primary_key=True, editable=False, unique=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    comment = models.TextField(blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.blog
    
    class Meta:
        ordering = ['blog', 'date_posted']
        verbose_name_plural = 'Comments'

class TherapistRateScores(models.Model):
    id = models.CharField(max_length=30, primary_key=True, editable=False, unique=True)
    therapist = models.ForeignKey(Therapists, on_delete=models.CASCADE, editable=False)
    rating = models.PositiveIntegerField(default=0, editable=False)
    feedback = models.TextField(null=True, blank=True)
    voting_date = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.therapist
    
    class Meta:
        ordering = ['therapist', 'voting_date']
        verbose_name_plural = 'Therapists rating'

