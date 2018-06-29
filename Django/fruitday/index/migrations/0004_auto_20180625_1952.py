# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-25 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180624_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelOptions(
            name='goodtype',
            options={'verbose_name': '商品类型', 'verbose_name_plural': '商品类型'},
        ),
        migrations.AddField(
            model_name='goods',
            name='good_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.GoodType'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='是否激活'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(upload_to='static/upload/goods', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='spec',
            field=models.CharField(max_length=50, verbose_name='商品规格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(max_length=30, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='goodtype',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='类型描述'),
        ),
        migrations.AlterField(
            model_name='goodtype',
            name='picture',
            field=models.ImageField(upload_to='static/upload/goodstype', verbose_name='类型图片'),
        ),
        migrations.AlterField(
            model_name='goodtype',
            name='title',
            field=models.CharField(max_length=30, verbose_name='类型名称'),
        ),
    ]