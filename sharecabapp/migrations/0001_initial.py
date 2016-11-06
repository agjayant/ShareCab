# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('destination', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('ridetime', models.DateTimeField(verbose_name=b'leave time')),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='ridegroup',
            field=models.ForeignKey(to='sharecabapp.Ride'),
        ),
    ]
