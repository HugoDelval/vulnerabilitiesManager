# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0008_auto_20150716_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulnerabilite',
            name='activites_liees',
            field=models.ManyToManyField(to='vuln.ActiviteAudit'),
        ),
    ]
