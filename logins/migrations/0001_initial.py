# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('initiated', models.DateTimeField(unique=True)),
                ('login', models.CharField(max_length=20)),
                ('ip', models.CharField(max_length=60)),
            ],
        ),
    ]
