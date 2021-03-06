# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-16 23:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import profiler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accidentform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_victim', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=2)),
                ('place', models.CharField(max_length=100)),
                ('accident_type', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=10, null=True)),
                ('victims_image', models.ImageField(blank=True, height_field='victims_height_field', null=True, upload_to=profiler.models.upload_location, width_field='victims_width_field')),
                ('victims_height_field', models.IntegerField(default=0)),
                ('victims_width_field', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='bloodform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='membersform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members_image', models.ImageField(blank=True, height_field='members_height_field', null=True, upload_to=profiler.models.upload_location, width_field='members_width_field')),
                ('members_height_field', models.IntegerField(default=0)),
                ('members_width_field', models.IntegerField(default=0)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('midname', models.CharField(max_length=100)),
                ('barangay', models.CharField(max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('age', models.CharField(max_length=2)),
                ('mobile', models.CharField(max_length=13)),
                ('civilstatus', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=100)),
                ('bloodtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiler.bloodform')),
            ],
        ),
        migrations.CreateModel(
            name='teamform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='membersform',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiler.teamform'),
        ),
        migrations.AddField(
            model_name='accidentform',
            name='team_incharge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiler.teamform'),
        ),
    ]
