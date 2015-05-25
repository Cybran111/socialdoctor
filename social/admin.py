from django.contrib import admin

# Register your models here.
from social.models import Feedback, UserProfile, Message, MessageNotification

admin.site.register((UserProfile, Feedback, Message, MessageNotification))
