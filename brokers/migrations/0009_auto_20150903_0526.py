# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0008_deal_shipper_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker_info',
            name='lat',
            field=models.DecimalField(default=72.12, max_digits=12, decimal_places=9, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='broker_info',
            name='lon',
            field=models.DecimalField(default=72.16, max_digits=12, decimal_places=9, blank=True),
            preserve_default=False,
        ),
    ]
