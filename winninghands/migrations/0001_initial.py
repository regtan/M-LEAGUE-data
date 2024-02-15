# Generated by Django 5.0.1 on 2024-02-15 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0003_member_organization'),
        ('rounds', '0005_delete_winninghand'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinningHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winning_type', models.CharField(choices=[('TSUMO', 'ツモ'), ('RON', 'ロン')], max_length=255, verbose_name='tsumo ron')),
                ('is_dealer', models.BooleanField(verbose_name='is dealer')),
                ('winning_hands', models.CharField(max_length=255, verbose_name='winning hands')),
                ('winning_pai', models.CharField(max_length=255, verbose_name='winning hands')),
                ('fuu', models.IntegerField(verbose_name='fuu')),
                ('faan', models.IntegerField(verbose_name='faan')),
                ('winning_score', models.IntegerField(editable=False, verbose_name='winning score')),
                ('additional_score', models.IntegerField(editable=False, verbose_name='additional score')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rounds.round')),
            ],
        ),
    ]