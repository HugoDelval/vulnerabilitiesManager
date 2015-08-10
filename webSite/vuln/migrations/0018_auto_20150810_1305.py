# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0017_auto_20150810_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommandation',
            name='themes',
            field=models.ManyToManyField(to='vuln.ThemeReco', blank=True),
        ),
    ]
