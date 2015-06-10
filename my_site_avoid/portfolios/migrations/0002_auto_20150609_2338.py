# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliocreation',
            name='title',
            field=models.CharField(unique=True, max_length=250, blank=True),
        ),
    ]
