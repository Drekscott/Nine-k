# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninek_site', '0015_category_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('images', models.ImageField(upload_to=b'img')),
                ('audio', models.FileField(upload_to=b'img')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('social_media', models.URLField()),
            ],
        ),
    ]
