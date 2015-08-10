# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0016_auto_20150810_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeReco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='recommandation',
            name='themes',
            field=models.ManyToManyField(to='vuln.ThemeReco', null=True, blank=True),
        ),
    ]
