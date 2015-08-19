# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0025_auto_20150819_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerabilite',
            name='definition',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vulnerabilite',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
