from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea, ModelChoiceField, Select
from django.forms import ChoiceField
from social.models import UserProfile, Feedback

class SearchForm(forms.Form):
    username = forms.CharField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['doctor_type', 'is_doctor']
        widgets = {'doctor_type': Select(choices=UserProfile.TYPE_CHOICES, attrs={'class': "form-control"})}


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'rating']

