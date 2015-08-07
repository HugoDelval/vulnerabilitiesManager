# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0014_auto_20150729_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerabilite',
            name='rapports_ou_on_a_trouve_la_vuln',
            field=models.ManyToManyField(to='vuln.Rapport', blank=True),
        ),
    ]
