# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0019_recommandation_rapports_ou_on_a_trouve_la_reco'),
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
