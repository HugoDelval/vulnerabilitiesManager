# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0023_auto_20150819_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerabilite',
            name='definition',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
