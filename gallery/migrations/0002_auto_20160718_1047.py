# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/photo-gallery')),
                ('link', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
