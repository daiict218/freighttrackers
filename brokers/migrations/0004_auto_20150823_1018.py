# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0003_auto_20150822_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='broker_info',
            old_name='comapnyname',
            new_name='comapanyname',
        ),
    ]
