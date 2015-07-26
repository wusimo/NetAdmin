# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='account',
            name='courses_caught',
        ),
        migrations.RemoveField(
            model_name='account',
            name='courses_pack',
        ),
        migrations.RemoveField(
            model_name='account',
            name='courses_used',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_premium',
        ),
        migrations.AddField(
            model_name='account',
            name='is_TA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_parents',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
