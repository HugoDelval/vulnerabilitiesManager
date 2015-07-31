# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0002_auto_20150715_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiviteAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_activite', models.CharField(max_length=255)),
                ('activiteEnfante', models.ForeignKey(related_name='activiteParente', to='vuln.ActiviteAudit')),
            ],
        ),
        migrations.RenameField(
            model_name='recommandation',
            old_name='difficulte_mise_en_place',
            new_name='cout_reco',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='nom_type_rapport',
        ),
        migrations.AddField(
            model_name='difficultereco',
            name='cout_homme_mois',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='difficultereco',
            name='cout_initial_euros',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='difficultereco',
            name='cout_recurrent_euros',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
