# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0010_remove_broker_info_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broker_info',
            name='pincode',
        ),
    ]
