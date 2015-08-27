# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gps_track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.DecimalField(max_digits=8, decimal_places=3)),
                ('lat', models.DecimalField(max_digits=8, decimal_places=3)),
                ('gps', models.ForeignKey(to='brokers.gps_info')),
            ],
        ),
        migrations.AddField(
            model_name='truck_info',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]
