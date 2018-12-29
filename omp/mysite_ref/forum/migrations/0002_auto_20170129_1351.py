# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='reply',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
