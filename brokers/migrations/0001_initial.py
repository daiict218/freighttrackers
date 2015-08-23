# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broker_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.IntegerField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^.{6}$', message=b'Length has to be 6', code=b'nomatch')])),
                ('contact_number', models.BigIntegerField(max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('comapnyname', models.CharField(max_length=30)),
                ('rating', models.IntegerField(default=0)),
                ('email_status', models.BooleanField(default=False)),
                ('mobile_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='verification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=50)),
                ('number', models.IntegerField(max_length=10)),
                ('broker_id', models.ForeignKey(to='brokers.Broker_info')),
            ],
        ),
    ]
