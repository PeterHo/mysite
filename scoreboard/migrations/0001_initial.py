# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('winner', models.CharField(default=b'H', max_length=50, verbose_name=b'\xe8\x83\x9c\xe8\x80\x85', choices=[(b'H', b'\xe4\xbd\x95'), (b'Y', b'\xe4\xbd\x99'), (b'Z', b'\xe5\xbc\xa0')])),
                ('loser', models.CharField(default=b'H', max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\x80\x85', choices=[(b'H', b'\xe4\xbd\x95'), (b'Y', b'\xe4\xbd\x99'), (b'Z', b'\xe5\xbc\xa0')])),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xaf\x94\xe8\xb5\x9b\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
