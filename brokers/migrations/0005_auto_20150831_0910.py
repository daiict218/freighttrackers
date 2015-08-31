# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0004_auto_20150827_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='load_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=30)),
                ('destinaton', models.CharField(max_length=30)),
                ('pickupdate', models.DateField()),
                ('loadtype', models.CharField(max_length=30)),
                ('quantity', models.CharField(max_length=30)),
                ('numoftruck', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipper_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=30, blank=True)),
                ('contact_number', models.BigIntegerField()),
                ('email_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='load_info',
            name='shipper',
            field=models.ForeignKey(to='brokers.Shipper_info'),
        ),
    ]
