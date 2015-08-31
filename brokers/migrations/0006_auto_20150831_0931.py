# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0005_auto_20150831_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='load_info',
            old_name='destinaton',
            new_name='destination',
        ),
    ]
