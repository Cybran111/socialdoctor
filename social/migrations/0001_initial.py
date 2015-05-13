# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.TextField(choices=[(b'doctor', b'Doctor'), (b'patient', b'Patient')])),
                ('feedback', models.ManyToManyField(related_name='user_feedbacks', through='social.Feedback', to='social.UserProfile')),
                ('following', models.ManyToManyField(to='social.UserProfile', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(related_name='feedback_author', to='social.UserProfile'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='estimated',
            field=models.ForeignKey(related_name='feedback_estimated', to='social.UserProfile'),
        ),
    ]
