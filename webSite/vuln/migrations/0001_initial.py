# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiviteAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_activite', models.CharField(max_length=255)),
                ('activiteParente', models.ForeignKey(related_name='activiteEnfante', blank=True, to='vuln.ActiviteAudit', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DifficulteExploitVuln',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('niveau', models.IntegerField()),
                ('description_niveau', models.CharField(max_length=255)),
                ('description_acte_volontaire', models.TextField()),
                ('description_acte_involontaire', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DifficulteReco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('niveau', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('cout_homme_mois', models.FloatField(default=0)),
                ('cout_initial_euros', models.FloatField(default=0)),
                ('cout_recurrent_euros', models.FloatField(default=0)),
                ('description_detaillee', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EcheanceReco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('niveau', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('description_detaillee', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImpactVuln',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('niveau', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('description_detaillee', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MotClef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_rapport', models.CharField(max_length=255)),
                ('date_rapport', models.DateField()),
                ('auditeurs_impliques', models.TextField()),
            ],
            options={
                'ordering': ['nom_rapport'],
            },
        ),
        migrations.CreateModel(
            name='Recommandation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('explication', models.TextField()),
                ('cout_reco', models.ForeignKey(to='vuln.DifficulteReco')),
                ('echeance', models.ForeignKey(to='vuln.EcheanceReco')),
                ('rapports_ou_on_a_trouve_la_reco', models.ManyToManyField(to='vuln.Rapport', blank=True)),
                ('themes', models.ManyToManyField(to='vuln.MotClef', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerabilite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('definition', models.TextField(null=True, blank=True)),
                ('estBoiteNoire', models.BooleanField()),
                ('activites_liees', models.ManyToManyField(to='vuln.ActiviteAudit')),
                ('difficulte_exploit', models.ForeignKey(to='vuln.DifficulteExploitVuln')),
                ('impact', models.ForeignKey(to='vuln.ImpactVuln')),
                ('mots_clefs', models.ManyToManyField(to='vuln.MotClef')),
                ('rapports_ou_on_a_trouve_la_vuln', models.ManyToManyField(to='vuln.Rapport', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='recommandation',
            name='vuln',
            field=models.ForeignKey(blank=True, to='vuln.Vulnerabilite', null=True),
        ),
    ]
