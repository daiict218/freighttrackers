# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0007_driver_info_gps_info_truck_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truck_info',
            old_name='gps_id',
            new_name='gps',
        ),
    ]
