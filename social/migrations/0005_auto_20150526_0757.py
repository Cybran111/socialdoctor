# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_messagenotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='aboutme',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='qualification',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='workplace',
            field=models.TextField(blank=True),
        ),
    ]
