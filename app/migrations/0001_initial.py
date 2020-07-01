# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-28 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('status', models.CharField(choices=[('Not Scheduled', 'Not Scheduled'), ('Scheduled', 'Scheduled'), ('Finished', 'Finished')], default='Not Scheduled', max_length=20)),
                ('player_1_score', models.PositiveIntegerField(default=0)),
                ('player_2_score', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(default='static/img/teams/default-logo.png', upload_to=b'')),
                ('goal_scored', models.IntegerField(default=0)),
                ('no_of_matches', models.IntegerField(default=0)),
                ('no_of_matches_win', models.IntegerField(default=0)),
                ('match_dates', models.DateField(blank=True, null=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('team_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_name', to='app.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='app.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='app.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='app.Venue'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_won', to='app.Team'),
        ),
        migrations.AddField(
            model_name='manager',
            name='team_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_team_name', to='app.Team'),
        ),
        migrations.AddField(
            model_name='coach',
            name='team_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_team_name', to='app.Team'),
        ),
    ]
