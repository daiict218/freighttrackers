# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0006_auto_20150831_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.IntegerField()),
                ('Broker_info', models.ForeignKey(to='brokers.Broker_info')),
                ('load_info', models.ForeignKey(to='brokers.load_info')),
            ],
        ),
    ]
