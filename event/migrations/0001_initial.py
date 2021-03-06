# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_closed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(help_text=b'The event url, use all simple and - as a seperator, Eg: junkyard-wars')),
                ('private_slug', models.CharField(blank=True, default=b'', max_length=40)),
                ('quote', models.CharField(help_text=b'Text displayed on the cards in /events/', max_length=70)),
                ('info', models.TextField(help_text=b'Please write in Markdown (Editor: http://dillinger.io/)')),
                ('cash_prize', models.IntegerField(help_text=b'Numeric, Eg: 5000')),
                ('date', models.IntegerField(blank=True, help_text=b'20 or 21', max_length=2, null=True)),
                ('time', models.CharField(blank=True, help_text=b'(Start time), Eg: 9:00 am', max_length=30)),
                ('end_time', models.CharField(blank=True, help_text=b'(End Time), Eg: 4:00 pm', max_length=30, null=True)),
                ('venue', models.CharField(blank=True, help_text=b'Eg: Room 243, Block 2', max_length=50)),
                ('team_min', models.IntegerField(default=1, help_text=b'Minimum number of people in a team (If individual: 1)')),
                ('team_max', models.IntegerField(default=1, help_text=b'Maximum number of people in a team (If individual: 1)')),
                ('team_type', models.CharField(choices=[(b'individual', b'Individual'), (b'team', b'Team'), (b'group', b'Group')], default=b'individual', max_length=20)),
                ('technical', models.BooleanField(default=True, help_text=b'If cultural set to false')),
                ('tags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(b'cse', b'Computer Science'), (b'ec', b'Electronics'), (b'mech', b'Mechanical'), (b'civil', b'Civil')], max_length=17, null=True)),
                ('cover', models.URLField(blank=True, default=b'', help_text=b'imgur link for cover (1300x500)')),
                ('picture_one', models.URLField(blank=True, default=b'', help_text=b'imgur link for head one (100x100)')),
                ('picture_two', models.URLField(blank=True, default=b'', help_text=b'imgur link for head one (100x100)')),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-views'],
                'permissions': (('change_own', 'Change events incharge of'),),
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(blank=True, max_length=10, null=True)),
                ('is_owner', models.BooleanField(default=False)),
                ('on_spot', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mode', models.CharField(blank=True, default=b'online', max_length=50, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Profile')),
            ],
            options={
                'ordering': ['-created'],
                'permissions': (('own_event_registrations', 'View registrations for own event'),),
            },
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together=set([('event', 'profile')]),
        ),
    ]
