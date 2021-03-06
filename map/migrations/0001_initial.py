# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('has_supply_center', models.BooleanField()),
                ('has_coast', models.BooleanField()),
                ('is_neutral', models.BooleanField(default=False)),
                ('is_ocean', models.BooleanField(default=False)),
                ('neighbors', models.ManyToManyField(related_name='neighbors_rel_+', to='map.Region', blank=True)),
                ('owner', models.ForeignKey(blank=True, to='engine.PlayerNation', null=True)),
            ],
        ),
    ]
