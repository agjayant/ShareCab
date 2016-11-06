# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharecabapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='ridegroup',
        ),
        migrations.AddField(
            model_name='ride',
            name='email',
            field=models.EmailField(default=b'abc@xyz.com', max_length=254),
        ),
        migrations.AddField(
            model_name='ride',
            name='name',
            field=models.CharField(default=b'-', max_length=50),
        ),
        migrations.AddField(
            model_name='ride',
            name='preference',
            field=models.CharField(default=b'Te', max_length=10, choices=[(b'Au', b'Auto'), (b'Te', b'Tempo'), (b'Ca', b'Cab'), (b'An', b'Any')]),
        ),
        migrations.AddField(
            model_name='ride',
            name='train',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ride',
            name='destination',
            field=models.CharField(default=b'CNB', max_length=30),
        ),
        migrations.AlterField(
            model_name='ride',
            name='source',
            field=models.CharField(default=b'IITK', max_length=30),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
