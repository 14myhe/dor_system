# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dor', '0002_stu'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('sno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=20)),
                ('college_no', models.CharField(max_length=20)),
                ('major_no', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1)),
                ('dor_no', models.CharField(max_length=10)),
                ('room_no', models.CharField(max_length=10)),
                ('mobilephone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]