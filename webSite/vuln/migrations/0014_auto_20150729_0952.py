# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0013_auto_20150722_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rapport',
            options={'ordering': ['nom_rapport']},
        ),
    ]
