from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Profile(models.Model):
    TYPE_CHOICES = (
        ("doctor", 'Doctor'),
        ('patient', 'Patient'),
    )

    user = models.OneToOneField(get_user_model())
    followers = models.ManyToManyField(get_user_model())
    user_type = models.TextField(choices=TYPE_CHOICES)