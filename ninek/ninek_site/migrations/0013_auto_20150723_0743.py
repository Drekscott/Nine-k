# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninek_site', '0012_auto_20150723_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_pic',
            field=models.ImageField(upload_to=b'static'),
        ),
        migrations.AlterField(
            model_name='page',
            name='upload_image',
            field=models.ImageField(upload_to=b'static'),
        ),
    ]
