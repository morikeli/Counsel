from django.contrib import admin
from .models import Feedback, UserProfile, YourStory, AskQuestion, UserAppointment

admin.site.register(UserProfile)
admin.site.register(YourStory)
admin.site.register(AskQuestion)
admin.site.register(UserAppointment)
admin.site.register(Feedback)
