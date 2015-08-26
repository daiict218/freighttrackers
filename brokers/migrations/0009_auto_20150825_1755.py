# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0008_auto_20150824_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver_info',
            old_name='licence_number',
            new_name='license_number',
        ),
        migrations.RenameField(
            model_name='truck_info',
            old_name='number1',
            new_name='numberone',
        ),
        migrations.RenameField(
            model_name='truck_info',
            old_name='number2',
            new_name='numbertwo',
        ),
        migrations.AddField(
            model_name='driver_info',
            name='broker',
            field=models.ForeignKey(default=1, to='brokers.Broker_info'),
            preserve_default=False,
        ),
    ]
