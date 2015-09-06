# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0009_auto_20150903_0526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broker_info',
            name='address',
        ),
    ]
