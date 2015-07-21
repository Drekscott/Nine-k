# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about_name', models.CharField(max_length=120)),
                ('about_me', models.TextField()),
                ('about_pic', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('author_name', models.CharField(max_length=120)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('upload_image', models.ImageField(upload_to=None)),
                ('page_content', models.TextField()),
                ('category', models.ForeignKey(to='ninek_site.Category')),
            ],
        ),
    ]
