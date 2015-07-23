# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150722_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motclef',
            name='nom',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
