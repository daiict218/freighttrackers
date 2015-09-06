# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0014_auto_20150903_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='load_info',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='load_info',
            name='lon',
        ),
        migrations.AddField(
            model_name='shipper_info',
            name='lat',
            field=models.DecimalField(default=72.021, max_digits=12, decimal_places=9, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipper_info',
            name='lon',
            field=models.DecimalField(default=72.01, max_digits=12, decimal_places=9, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipper_info',
            name='updatelocation',
            field=models.BooleanField(default=False),
        ),
    ]
