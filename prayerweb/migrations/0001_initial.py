# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import prayerweb.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('topic', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sunday', models.DateField(validators=[prayerweb.validators.validate_sunday])),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
