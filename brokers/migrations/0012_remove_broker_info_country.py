# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0011_remove_broker_info_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broker_info',
            name='country',
        ),
    ]