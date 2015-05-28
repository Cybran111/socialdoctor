# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea, ModelChoiceField, Select, CheckboxInput
from django.forms import ChoiceField
from social.models import UserProfile, Feedback, Message


class SearchForm(forms.Form):
    username = forms.CharField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('qualification', 'education', 'workplace', 'aboutme')

        labels = {
            'qualification': u'Кваліфікація',
            'education': u"Освіта",
            'workplace': u"Місце роботи",
            'aboutme': u"Про себе"
        }

        widgets = {
            'qualification': Textarea(attrs={'cols': 40, 'rows': 5}),
            'education': Textarea(attrs={'cols': 40, 'rows': 5}),
            'workplace': Textarea(attrs={'cols': 40, 'rows': 5}),
            'aboutme': Textarea(attrs={'cols': 40, 'rows': 5})}


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('aboutme',)
        labels = {'aboutme': u'Про себе'}
        widgets = {'aboutme': Textarea(attrs={'cols': 40, 'rows': 5})}


class MessageForm(forms.Form):
        text = forms.CharField(label="Текст повідомлення")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['doctor_type', 'is_doctor']
        widgets = {
            'is_doctor': CheckboxInput(attrs={'onclick': "enable()"}),
            'doctor_type': Select(choices=UserProfile.TYPE_CHOICES, attrs={'class': "form-control", 'disabled': ""})
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'rating']

