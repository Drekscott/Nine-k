# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninek_site', '0003_about_about_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_pic',
            field=models.ImageField(default=0, upload_to=None),
            preserve_default=False,
        ),
    ]
