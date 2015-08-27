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
                ('address', models.CharField(max_length=30, blank=True)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30, blank=True)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.IntegerField(validators=[django.core.validators.RegexValidator(regex=b'^.{6}$', message=b'Length has to be 6', code=b'nomatch')])),
                ('contact_number', models.BigIntegerField()),
                ('password', models.CharField(max_length=50)),
                ('companyname', models.CharField(max_length=30)),
                ('rating', models.IntegerField(default=0)),
                ('email_status', models.BooleanField(default=True)),
                ('mobile_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='driver_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.IntegerField(validators=[django.core.validators.RegexValidator(regex=b'^.{6}$', message=b'Length has to be 6', code=b'nomatch')])),
                ('contact_number', models.BigIntegerField()),
                ('license_number', models.CharField(max_length=30)),
                ('age', models.IntegerField(max_length=2)),
                ('broker', models.ForeignKey(to='brokers.Broker_info')),
            ],
        ),
        migrations.CreateModel(
            name='gps_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='truck_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=2)),
                ('rto', models.CharField(max_length=3)),
                ('numberone', models.CharField(max_length=3, blank=True)),
                ('numbertwo', models.IntegerField(max_length=4)),
                ('truck_type', models.CharField(max_length=30)),
                ('truck_model', models.CharField(max_length=30)),
                ('truck_tyre', models.IntegerField(max_length=4)),
                ('Capacity', models.IntegerField(max_length=10)),
                ('body_length', models.IntegerField(max_length=10)),
                ('body_width', models.IntegerField(max_length=10)),
                ('pref_item', models.CharField(max_length=30)),
                ('rc_book', models.FileField(upload_to=b'documents/rc/')),
                ('puc_book', models.FileField(upload_to=b'documents/puc/')),
                ('insurance_book', models.FileField(upload_to=b'documents/insurance/')),
                ('broker', models.ForeignKey(to='brokers.Broker_info')),
                ('driver', models.ForeignKey(to='brokers.driver_info')),
                ('gps', models.ForeignKey(to='brokers.gps_info')),
            ],
        ),
        migrations.CreateModel(
            name='verification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('broker_id', models.ForeignKey(to='brokers.Broker_info')),
            ],
        ),
    ]
