# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0009_auto_20150825_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker_info',
            name='address',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='broker_info',
            name='state',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
