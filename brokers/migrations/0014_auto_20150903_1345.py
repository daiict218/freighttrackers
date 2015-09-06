# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0013_broker_info_updatelocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='load_info',
            name='lat',
            field=models.DecimalField(default=72.02, max_digits=12, decimal_places=9, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='load_info',
            name='lon',
            field=models.DecimalField(default=72.06, max_digits=12, decimal_places=9, blank=True),
            preserve_default=False,
        ),
    ]
