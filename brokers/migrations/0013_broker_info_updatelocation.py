# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0012_remove_broker_info_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker_info',
            name='updatelocation',
            field=models.BooleanField(default=False),
        ),
    ]
