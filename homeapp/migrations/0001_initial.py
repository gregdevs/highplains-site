# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ourprojectsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutus_headline', models.CharField(max_length=140)),
                ('aboutus_desc', models.TextField(default='About US Description')),
            ],
        ),
        migrations.CreateModel(
            name='HomeBucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket_title', models.CharField(max_length=140)),
                ('bucket_image', models.CharField(default='bucket_image', max_length=300)),
                ('bucket_desc', models.TextField(default='bucket_desc')),
            ],
        ),
        migrations.CreateModel(
            name='HomeProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourprojectsapp.OurProject')),
            ],
        ),
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav_item', models.CharField(max_length=50)),
                ('nav_position', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['nav_position'],
            },
        ),
    ]
