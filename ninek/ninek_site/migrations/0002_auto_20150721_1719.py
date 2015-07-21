# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('ninek_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='uuid.uuid4', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic',
            field=models.ImageField(upload_to=b'ninek_site'),
        ),
        migrations.AlterField(
            model_name='page',
            name='upload_image',
            field=models.ImageField(upload_to=b'ninek_site'),
        ),
    ]
