from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class CounsellorProfile(models.Model):
    id = models.CharField(max_length=15, editable=False, unique=True, primary_key=True)
    counsellor = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    dp = models.ImageField(default='default.jpg', upload_to='Counsellors-Dps')
    dob = models.DateField(null=True)
    age = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=30, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    gender = models.CharField(max_length=10, blank=False)
    marital_status = models.CharField(max_length=15, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.counsellor}'
    
    def save(self, *args, **kwargs):
        super(CounsellorProfile, self).save(*args, **kwargs)

        user_dp = Image.open(self.dp.path)
        
        if user_dp.height > 500 and user_dp.width > 500:
            output_size = (500, 500)
            user_dp.thumbnail(output_size)
            user_dp.save(self.dp.path)
    
    class Meta:
        verbose_name_plural = 'Counsellors'
        ordering = ['counsellor']
        
        
class WorkProfile(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    org = models.CharField(max_length=50, db_column='Place of Work')
    mobile_no = models.CharField(max_length=14, blank=False)
    location = models.CharField(max_length=30)
    role = models.CharField(max_length=50, blank=False)
    opening_hours = models.TimeField(blank=False, null=True)
    closing_hours = models.TimeField(blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = 'Places of work'
        ordering = ['org']
        

class LogBook(models.Model):
    id = models.CharField(max_length=10, primary_key=True, editable=False)
    log_name = models.ForeignKey(CounsellorProfile, on_delete=models.CASCADE)
    patient = models.TextField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.counsellor}'
    
    class Meta:
        verbose_name_plural = 'Log Book'
        ordering = ['created']
        