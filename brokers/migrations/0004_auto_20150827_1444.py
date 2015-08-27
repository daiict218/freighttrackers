# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0003_auto_20150827_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gps_track',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='gps_track',
            name='lon',
        ),
        migrations.AddField(
            model_name='gps_track',
            name='dest_city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gps_track',
            name='dest_state',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gps_track',
            name='source_city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gps_track',
            name='source_state',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
