# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=40)),
                ('deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='spending',
            name='id_user',
            field=models.ForeignKey(to='tracker.User'),
        ),
    ]
