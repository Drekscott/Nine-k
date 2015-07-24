# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninek_site', '0014_auto_20150723_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pic',
            field=models.ImageField(default=0, upload_to=b'img'),
            preserve_default=False,
        ),
    ]
