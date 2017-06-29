# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chesseditor', '0002_auto_20170621_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moves',
            name='chessman',
            field=models.CharField(choices=[('biała wieża a1', 'a1_w_rook'), ('h1_w_rook', 'biała wieża h1'), ('b1_w_knight', 'biały skoczek b1'), ('g1_w_knight', 'biały skoczek g1'), ('c1_w_bishop', 'biały goniec c1'), ('f1_w_bishop', 'biały goniec f1'), ('d1_w_queen', 'biały hetman d1'), ('e1_w_king', 'biały król e1'), ('a2_w_pawn', 'biały pion a2'), ('b2_w_pawn', 'biały pion b2'), ('c2_w_pawn', 'biały pion c2'), ('d2_w_pawn', 'biały pion d2'), ('e2_w_pawn', 'biały pion e2'), ('f2_w_pawn', 'biały pion f2'), ('g2_w_pawn', 'biały pion g2'), ('h2_w_pawn', 'biały pion h2'), ('a8_b_rook', 'czarna wieża a1'), ('h8_b_rook', 'czarna wieża h8'), ('b8_b_knight', 'czarny skoczek b1'), ('g8_b_knight', 'czarny skoczek g8'), ('c8_b_knight', 'czarny goniec c1'), ('f8_b_bishop', 'czarny goniec f8'), ('d8_b_queen', 'czarny hetman d1'), ('e8_b_king', 'czarny król e8'), ('a7_b_pawn', 'czarny pion a7'), ('b7_b_pawn', 'czarny pion b7'), ('c7_b_pawn', 'czarny pion c7'), ('d7_b_pawn', 'czarny pion d7'), ('e7_b_pawn', 'czarny pion e7'), ('f7_b_pawn', 'czarny pion f7'), ('g7_b_pawn', 'czarny pion g7'), ('h7_b_pawn', 'czarny pion h7')], default='pionek', max_length=30, verbose_name='Figura Szachowa'),
        ),
        migrations.AlterField(
            model_name='state',
            name='chessman',
            field=models.CharField(choices=[('biała wieża a1', 'a1_w_rook'), ('h1_w_rook', 'biała wieża h1'), ('b1_w_knight', 'biały skoczek b1'), ('g1_w_knight', 'biały skoczek g1'), ('c1_w_bishop', 'biały goniec c1'), ('f1_w_bishop', 'biały goniec f1'), ('d1_w_queen', 'biały hetman d1'), ('e1_w_king', 'biały król e1'), ('a2_w_pawn', 'biały pion a2'), ('b2_w_pawn', 'biały pion b2'), ('c2_w_pawn', 'biały pion c2'), ('d2_w_pawn', 'biały pion d2'), ('e2_w_pawn', 'biały pion e2'), ('f2_w_pawn', 'biały pion f2'), ('g2_w_pawn', 'biały pion g2'), ('h2_w_pawn', 'biały pion h2'), ('a8_b_rook', 'czarna wieża a1'), ('h8_b_rook', 'czarna wieża h8'), ('b8_b_knight', 'czarny skoczek b1'), ('g8_b_knight', 'czarny skoczek g8'), ('c8_b_knight', 'czarny goniec c1'), ('f8_b_bishop', 'czarny goniec f8'), ('d8_b_queen', 'czarny hetman d1'), ('e8_b_king', 'czarny król e8'), ('a7_b_pawn', 'czarny pion a7'), ('b7_b_pawn', 'czarny pion b7'), ('c7_b_pawn', 'czarny pion c7'), ('d7_b_pawn', 'czarny pion d7'), ('e7_b_pawn', 'czarny pion e7'), ('f7_b_pawn', 'czarny pion f7'), ('g7_b_pawn', 'czarny pion g7'), ('h7_b_pawn', 'czarny pion h7')], default='pionek', max_length=30, verbose_name='Figura Szachowa'),
        ),
    ]