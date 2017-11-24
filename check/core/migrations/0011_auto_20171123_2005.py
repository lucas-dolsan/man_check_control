# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 22:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='terceiro',
            name='bairro',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terceiro',
            name='cep',
            field=models.CharField(default=1, max_length=50, verbose_name='CEP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terceiro',
            name='cidade',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terceiro',
            name='data_cadastro',
            field=models.DateField(default=datetime.datetime(2017, 11, 23, 22, 5, 39, 773233, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terceiro',
            name='logradouro',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terceiro',
            name='numero',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terceiro',
            name='uf',
            field=models.CharField(default=1, max_length=2, verbose_name='UF'),
            preserve_default=False,
        ),
    ]