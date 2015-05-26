# coding=utf-8
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    TYPE_CHOICES = (
        ("surgeon", 'хірург'),
        ("pediatrician", "педіатр"),
        ("therapist", "терапевт"),
        ("dentist", "стоматолог"),
        ("ophthalmologist", "офтальмолог"),
        ("psychiatrist", "психіатр"),
        ("neurologist", "невролог"),
    )

    user = models.OneToOneField(User)
    is_doctor = models.BooleanField()
    following = models.ManyToManyField("self", symmetrical=False, blank=True)
    feedback = models.ManyToManyField("UserProfile", through="Feedback",
                                      through_fields=('author', 'estimated'),
                                      related_name="user_feedbacks")
    doctor_type = models.TextField(choices=TYPE_CHOICES, blank=True)

    qualification = models.TextField(blank=True)
    education = models.TextField(blank=True)
    workplace = models.TextField(blank=True)
    aboutme = models.TextField(blank=True)

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


class Message(models.Model):
    from_person = models.ForeignKey(UserProfile, related_name="message_from")
    to_person = models.ForeignKey(UserProfile, related_name="message_to")
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __unicode__(self):
        return "From: %s, To: %s, Text: %s" % (self.from_person, self.to_person, self.text)


class MessageNotification(models.Model):
    from_person = models.ForeignKey(UserProfile, related_name="notify_from")
    to_person = models.ForeignKey(UserProfile, related_name="notify_to")

    def __unicode__(self):
        return "From: %s, To: %s" % (self.from_person, self.to_person)
