# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninek_site', '0016_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='audio',
            field=models.FileField(upload_to=b'img', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='social_media',
            field=models.URLField(blank=True),
        ),
    ]
