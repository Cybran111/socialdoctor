# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20150521_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='doctor_type',
            field=models.TextField(blank=True, choices=[(b'surgeon', b'\xd1\x85\xd1\x96\xd1\x80\xd1\x83\xd1\x80\xd0\xb3'), (b'pediatrician', b'\xd0\xbf\xd0\xb5\xd0\xb4\xd1\x96\xd0\xb0\xd1\x82\xd1\x80'), (b'therapist', b'\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd0\xbf\xd0\xb5\xd0\xb2\xd1\x82'), (b'dentist', b'\xd1\x81\xd1\x82\xd0\xbe\xd0\xbc\xd0\xb0\xd1\x82\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3'), (b'ophthalmologist', b'\xd0\xbe\xd1\x84\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbc\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3'), (b'psychiatrist', b'\xd0\xbf\xd1\x81\xd0\xb8\xd1\x85\xd1\x96\xd0\xb0\xd1\x82\xd1\x80'), (b'neurologist', b'\xd0\xbd\xd0\xb5\xd0\xb2\xd1\x80\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3')]),
        ),
        migrations.AddField(
            model_name='message',
            name='from_person',
            field=models.ForeignKey(related_name='message_from', to='social.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='to_person',
            field=models.ForeignKey(related_name='message_to', to='social.UserProfile'),
        ),
    ]
