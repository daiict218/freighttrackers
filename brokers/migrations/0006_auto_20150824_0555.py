# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0005_auto_20150823_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker_info',
            name='email_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='broker_info',
            name='mobile_status',
            field=models.BooleanField(default=True),
        ),
    ]
