# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='loser',
            field=models.CharField(default=b'H', max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\x80\x85', choices=[(b'\xe4\xbd\x95', b'\xe4\xbd\x95'), (b'\xe4\xbd\x99', b'\xe4\xbd\x99'), (b'\xe5\xbc\xa0', b'\xe5\xbc\xa0')]),
        ),
        migrations.AlterField(
            model_name='score',
            name='winner',
            field=models.CharField(default=b'H', max_length=50, verbose_name=b'\xe8\x83\x9c\xe8\x80\x85', choices=[(b'\xe4\xbd\x95', b'\xe4\xbd\x95'), (b'\xe4\xbd\x99', b'\xe4\xbd\x99'), (b'\xe5\xbc\xa0', b'\xe5\xbc\xa0')]),
        ),
    ]
