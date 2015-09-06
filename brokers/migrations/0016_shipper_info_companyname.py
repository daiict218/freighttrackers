# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0015_auto_20150904_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipper_info',
            name='companyname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
