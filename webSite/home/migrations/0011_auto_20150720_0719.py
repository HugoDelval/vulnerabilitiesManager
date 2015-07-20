# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150720_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rapport',
            name='vulnerabilites_identifiees',
        ),
        migrations.AddField(
            model_name='vulnerabilite',
            name='rapports_ou_on_a_trouve_la_vuln',
            field=models.ManyToManyField(to='home.Rapport'),
        ),
    ]
