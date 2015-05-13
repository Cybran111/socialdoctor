from django.contrib import admin

# Register your models here.
from social.models import Feedback
from social.models import UserProfile

admin.site.register((UserProfile, Feedback))