from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    TYPE_CHOICES = (
        ("doctor", 'Doctor'),
        ('patient', 'Patient'),
    )

    user = models.OneToOneField(User)
    following = models.ManyToManyField("self", symmetrical=False, blank=True)
    feedback = models.ManyToManyField("UserProfile", through="Feedback",
                                      through_fields=('author', 'estimated'),
                                      related_name="feedbacks")
    user_type = models.TextField(choices=TYPE_CHOICES)

    def __unicode__(self):
        return self.user.username


class Feedback(models.Model):
    author = models.ForeignKey(UserProfile, related_name="author")
    estimated = models.ForeignKey(UserProfile, related_name='estimated')
    rating = models.IntegerField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)