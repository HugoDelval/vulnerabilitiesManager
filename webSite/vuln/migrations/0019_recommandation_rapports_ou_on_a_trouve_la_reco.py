# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0018_auto_20150810_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommandation',
            name='rapports_ou_on_a_trouve_la_reco',
            field=models.ManyToManyField(to='vuln.Rapport', blank=True),
        ),
    ]
