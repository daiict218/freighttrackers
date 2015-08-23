# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0004_auto_20150823_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='broker_info',
            old_name='comapanyname',
            new_name='companyname',
        ),
    ]
