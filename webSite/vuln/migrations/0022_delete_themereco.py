# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0021_themereco'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ThemeReco',
        ),
    ]
