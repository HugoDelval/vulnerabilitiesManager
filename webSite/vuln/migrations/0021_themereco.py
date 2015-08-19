# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0020_auto_20150819_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeReco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=255)),
            ],
        ),
    ]
