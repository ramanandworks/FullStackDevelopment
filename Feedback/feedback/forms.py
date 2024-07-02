from django import forms
from .models import Feedback
from django.core.exceptions import ValidationError

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback', 'question1', 'question2', 'question3']

    # Custom validation for the email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith ('@acharya.ac.in'):
            raise ValidationError('Email must be from the domain @acharya.ac.in')
        return email

    # Custom validation for the feedback field
    def clean_feedback(self):
        feedback = self.cleaned_data.get('feedback')
        prohibited_words = ['xyz', 'zzz']  # List of prohibited words
        for word in prohibited_words:
            if word in feedback:
                raise ValidationError(f'Feedback contains prohibited word: {word}')
        return feedback
