from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    TYPE_CHOICES = (
        ("doctor", 'Doctor'),
        ('patient', 'Patient'),
    )

    user = models.OneToOneField(User, related_name='related_user')
    followers = models.ManyToManyField(User)
    user_type = models.TextField(choices=TYPE_CHOICES)