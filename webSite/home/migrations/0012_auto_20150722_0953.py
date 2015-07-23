# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20150720_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='difficulteexploitvuln',
            name='description_niveau',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='difficultereco',
            name='description_detaillee',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='echeancereco',
            name='description_detaillee',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='impactvuln',
            name='description_detaillee',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='difficultereco',
            name='cout_homme_mois',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='difficultereco',
            name='cout_initial_euros',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='difficultereco',
            name='cout_recurrent_euros',
            field=models.FloatField(default=0),
        ),
    ]
