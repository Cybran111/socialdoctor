# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20150525_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_person', models.ForeignKey(related_name='notify_from', to='social.UserProfile')),
                ('to_person', models.ForeignKey(related_name='notify_to', to='social.UserProfile')),
            ],
        ),
    ]
