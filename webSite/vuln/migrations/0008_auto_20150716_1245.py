# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0007_auto_20150715_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motclef',
            name='vuln',
        ),
        migrations.AddField(
            model_name='vulnerabilite',
            name='mots_clefs',
            field=models.ManyToManyField(to='vuln.MotClef'),
        ),
    ]
