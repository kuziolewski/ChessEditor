# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chesseditor', '0003_auto_20170622_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moves',
            name='chessman',
            field=models.CharField(choices=[('biała wieża a1', 'biała wieża a1'), ('biała wieża h1', 'biała wieża h1'), ('biały skoczek b1', 'biały skoczek b1'), ('g1_w_knight', 'biały skoczek g1'), ('biały goniec c1', 'biały goniec c1'), ('biały goniec f1', 'biały goniec f1'), ('biały hetman d1', 'biały hetman d1'), ('biały król e1', 'biały król e1'), ('biały pion a2', 'biały pion a2'), ('biały pion b2', 'biały pion b2'), ('biały pion c2', 'biały pion c2'), ('biały pion d2', 'biały pion d2'), ('biały pion e2', 'biały pion e2'), ('biały pion f2', 'biały pion f2'), ('biały pion g2', 'biały pion g2'), ('biały pion h2', 'biały pion h2'), ('czarna wieża a1', 'czarna wieża a1'), ('czarna wieża h8', 'czarna wieża h8'), ('czarny skoczek b1', 'czarny skoczek b1'), ('czarny skoczek g8', 'czarny skoczek g8'), ('czarny goniec c1', 'czarny goniec c1'), ('czarny goniec f8', 'czarny goniec f8'), ('czarny hetman d1', 'czarny hetman d1'), ('czarny król e8', 'czarny król e8'), ('czarny pion a7', 'czarny pion a7'), ('czarny pion b7', 'czarny pion b7'), ('czarny pion c7', 'czarny pion c7'), ('czarny pion d7', 'czarny pion d7'), ('czarny pion e7', 'czarny pion e7'), ('czarny pion f7', 'czarny pion f7'), ('czarny pion g7', 'czarny pion g7'), ('czarny pion h7', 'czarny pion h7')], default='pionek', max_length=30, verbose_name='Figura Szachowa'),
        ),
        migrations.AlterField(
            model_name='state',
            name='chessman',
            field=models.CharField(choices=[('biała wieża a1', 'biała wieża a1'), ('biała wieża h1', 'biała wieża h1'), ('biały skoczek b1', 'biały skoczek b1'), ('g1_w_knight', 'biały skoczek g1'), ('biały goniec c1', 'biały goniec c1'), ('biały goniec f1', 'biały goniec f1'), ('biały hetman d1', 'biały hetman d1'), ('biały król e1', 'biały król e1'), ('biały pion a2', 'biały pion a2'), ('biały pion b2', 'biały pion b2'), ('biały pion c2', 'biały pion c2'), ('biały pion d2', 'biały pion d2'), ('biały pion e2', 'biały pion e2'), ('biały pion f2', 'biały pion f2'), ('biały pion g2', 'biały pion g2'), ('biały pion h2', 'biały pion h2'), ('czarna wieża a1', 'czarna wieża a1'), ('czarna wieża h8', 'czarna wieża h8'), ('czarny skoczek b1', 'czarny skoczek b1'), ('czarny skoczek g8', 'czarny skoczek g8'), ('czarny goniec c1', 'czarny goniec c1'), ('czarny goniec f8', 'czarny goniec f8'), ('czarny hetman d1', 'czarny hetman d1'), ('czarny król e8', 'czarny król e8'), ('czarny pion a7', 'czarny pion a7'), ('czarny pion b7', 'czarny pion b7'), ('czarny pion c7', 'czarny pion c7'), ('czarny pion d7', 'czarny pion d7'), ('czarny pion e7', 'czarny pion e7'), ('czarny pion f7', 'czarny pion f7'), ('czarny pion g7', 'czarny pion g7'), ('czarny pion h7', 'czarny pion h7')], default='pionek', max_length=30, verbose_name='Figura Szachowa'),
        ),
    ]