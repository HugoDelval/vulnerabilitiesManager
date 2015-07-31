# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DifficulteExploitVuln',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('niveau', models.IntegerField()),
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
            ],
        ),
        migrations.CreateModel(
            name='EcheanceReco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('niveau', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MotClef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_type_rapport', models.CharField(max_length=255)),
                ('nom_rapport', models.CharField(max_length=255)),
                ('date_rapport', models.DateField()),
                ('auditeurs_impliques', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recommandation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('explication', models.TextField()),
                ('difficulte_mise_en_place', models.ForeignKey(to='vuln.DifficulteReco')),
                ('echeance', models.ForeignKey(to='vuln.EcheanceReco')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerabilite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('estBoiteNoire', models.BooleanField()),
                ('difficulte_exploit', models.ForeignKey(to='vuln.DifficulteExploitVuln')),
                ('impact', models.ForeignKey(to='vuln.ImpactVuln')),
                ('rapport_associe', models.OneToOneField(to='vuln.Rapport')),
            ],
        ),
        migrations.AddField(
            model_name='recommandation',
            name='vuln',
            field=models.ForeignKey(to='vuln.Vulnerabilite'),
        ),
        migrations.AddField(
            model_name='motclef',
            name='vuln',
            field=models.ForeignKey(to='vuln.Vulnerabilite'),
        ),
    ]
