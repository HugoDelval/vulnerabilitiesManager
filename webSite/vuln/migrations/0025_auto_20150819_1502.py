# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0024_vulnerabilite_definition'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ThemeReco',
        ),
        migrations.AlterField(
            model_name='recommandation',
            name='themes',
            field=models.ManyToManyField(to='vuln.MotClef', blank=True),
        ),
    ]
