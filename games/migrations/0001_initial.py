# Generated by Django 5.0.1 on 2024-02-02 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game_days', '0002_alter_gameday_match_type'),
        ('members', '0003_member_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_number', models.IntegerField(verbose_name='game number')),
                ('game_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_days.gameday')),
                ('start_east', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_east', to='members.member')),
                ('start_north', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_north', to='members.member')),
                ('start_south', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_south', to='members.member')),
                ('start_west', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_west', to='members.member')),
            ],
        ),
    ]
