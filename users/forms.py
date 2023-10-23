from .models import Therapists, TherapySessions, Blogs, BlogComments, TherapistRateScores
from django import forms

class TherapistRegistrationForm(forms.ModelForm):
    workplace = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        help_text='Enter the name of hospital or school or facility you are currently working.',
    )
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-0',
        }),
        help_text='Enter mobile no. you use at your workplace.',
        label='Mobile number',
    )
    county = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        help_text='Enter county of your workplace',
    )
    sub_county = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        help_text='Enter sub-county of your workplace',
    )
    opening_hours = forms.TimeField(widget=forms.TimeInput(attrs={
            'type': 'time', 'class': 'mb-2',
        }),
    )
    closing_hours = forms.TimeField(widget=forms.TimeInput(attrs={
            'type': 'time', 'class': 'mb-2',
        }),
    )

    class Meta:
        model = Therapists
        fields = ['workplace', 'mobile_no', 'county', 'sub_county', 'opening_hours', 'closing_hours']

class BookTherapySessionForm(forms.ModelForm):
    SELECT_SESSION_TYPE = (
        (None, '-- Select session type --'),
        ('Physical', 'Physical session'),
        ('Virtual', 'Virtual session'),
    )
    session_type = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-0',
        }),
        help_text='Select a therapy session you prefer?',
        label='Therapy session',
    )

    class Meta:
        model = TherapySessions
        fields = ['session_type']

class ApproveTherapySessionForm(forms.ModelForm):
    SELECT_SESSION_TYPE = (
        (None, '-- Select session type --'),
        ('Physical', 'Physical session'),
        ('Virtual', 'Virtual session'),
    )
    therapist = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2'
        }),
        label="Therapist's name",
    )
    patient = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2'
        }),
        label="Patient's name",
    )
    session_type = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-0',
        }),
        help_text='Select a therapy session you prefer?',
        label='Therapy session',
    )
    appointment_date = forms.DateField(widget=forms.DateInput(atrrs={
        'type': 'date', 'class': 'mb-0',
        }),
        help_text='Schedule this session to the date of choice.',
    )
    appointment_time = forms.TimeField(widget=forms.TimeInput(atrrs={
        'type': 'time', 'class': 'mb-0',
        }),
        help_text='Schedule this session to the date of choice.',
    )

    class Meta:
        model = TherapySessions
        fields = ['therapist', 'patient', 'session_type', 'appointment_date', 'appointment_type']

class WriteBlogForm(forms.ModelForm):
    blog = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
    )
    attached_file = forms.FileField(widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'mb-2',
        }),
        help_text='You can attach an image, audio or a video file to your blog.',
        validators=[],
    )

    class Meta:
        model = Blogs
        fields = ['blog', 'attached_file']

class WriteBlogCommentsForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
    )

    class Meta:
        model = BlogComments
        fields = ['comment']

class RateTherapistsForm(forms.ModelForm):
    rating = forms.CharField(widget=forms.NumberInput(attrs={
            'type': 'number', 'class': 'mb-2',
        }),
    )
    feedback = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        help_text='Feel free to write a positive review or complaints about this therapist.'
    )

    class Meta:
        model = TherapistRateScores
        fields = ['rating', 'feedback']

# Edit forms.

class EditBlogForm(forms.ModelForm):
    blog = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
    )
    attached_file = forms.FileField(widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'mb-2',
        }),
        help_text='You can attach an image, audio or a video file to your blog.',
        validators=[],
    )

    class Meta:
        model = Blogs
        fields = ['blog', 'attached_file']

class EditCommentsForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
    )

    class Meta:
        model = BlogComments
        fields = ['comment']
