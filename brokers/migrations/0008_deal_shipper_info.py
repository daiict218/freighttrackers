# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0007_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='Shipper_info',
            field=models.ForeignKey(default=1, to='brokers.Shipper_info'),
            preserve_default=False,
        ),
    ]
