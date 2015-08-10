# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0015_auto_20150807_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommandation',
            name='vuln',
            field=models.ForeignKey(blank=True, to='vuln.Vulnerabilite', null=True),
        ),
    ]
