# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0009_vulnerabilite_activites_liees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerabilite',
            name='rapport_associe',
        ),
        migrations.AddField(
            model_name='rapport',
            name='vulnerabilites_identifiees',
            field=models.ManyToManyField(to='vuln.Vulnerabilite'),
        ),
    ]
