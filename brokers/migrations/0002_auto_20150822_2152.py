# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker_info',
            name='contact_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='broker_info',
            name='pincode',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(regex=b'^.{6}$', message=b'Length has to be 6', code=b'nomatch')]),
        ),
    ]
