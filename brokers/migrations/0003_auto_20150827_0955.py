# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0002_auto_20150827_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps_track',
            name='lat',
            field=models.DecimalField(max_digits=12, decimal_places=9),
        ),
        migrations.AlterField(
            model_name='gps_track',
            name='lon',
            field=models.DecimalField(max_digits=12, decimal_places=9),
        ),
    ]
