# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0002_auto_20150822_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='number',
            field=models.IntegerField(),
        ),
    ]
