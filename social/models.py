from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
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
                                      related_name="user_feedbacks")
    user_type = models.TextField(choices=TYPE_CHOICES)

    def __unicode__(self):
        return self.user.username


class Feedback(models.Model):
    author = models.ForeignKey(UserProfile, related_name="feedback_author")
    estimated = models.ForeignKey(UserProfile, related_name="feedback_estimated")
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "From: %s, To: %s, Text: %s, Rating: %d" % (self.author, self.estimated, self.text, self.rating)