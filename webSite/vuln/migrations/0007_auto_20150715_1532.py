# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0006_auto_20150715_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activiteaudit',
            name='activiteEnfante',
        ),
        migrations.AddField(
            model_name='activiteaudit',
            name='activiteParente',
            field=models.ForeignKey(related_name='activiteEnfante', blank=True, to='vuln.ActiviteAudit', null=True),
        ),
    ]
