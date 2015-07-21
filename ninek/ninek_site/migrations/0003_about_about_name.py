# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninek_site', '0002_remove_about_about_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_name',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
