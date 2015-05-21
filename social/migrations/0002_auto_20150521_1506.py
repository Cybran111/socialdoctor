# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_type',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='doctor_type',
            field=models.TextField(blank=True, choices=[(b'surgeon', b'\xd1\x85\xd1\x96\xd1\x80\xd1\x83\xd1\x80\xd0\xb3'), (b'pediatrician', b'\xd0\xbf\xd0\xb5\xd0\xb4\xd1\x96\xd0\xb0\xd1\x82\xd1\x80'), (b'therapist', b'\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd0\xbf\xd0\xb5\xd0\xb2\xd1\x82'), (b'dentist', b'\xd1\x81\xd1\x82\xd0\xbe\xd0\xbc\xd0\xb0\xd1\x82\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3'), (b'ophthalmologist', b'\xd0\xbe\xd1\x84\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbc\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3'), (b'psychiatrist', b'\xd0\xbf\xd1\x81\xd0\xb8\xd1\x85\xd1\x96\xd0\xb0\xd1\x82\xd1\x80')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_doctor',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
