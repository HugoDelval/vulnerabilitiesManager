# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150715_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activiteaudit',
            name='activiteEnfante',
            field=models.ForeignKey(related_name='activiteParente', blank=True, to='home.ActiviteAudit'),
        ),
    ]
