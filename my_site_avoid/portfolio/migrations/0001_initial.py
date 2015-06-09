# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCreation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('title', models.CharField(max_length=250, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('media', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
