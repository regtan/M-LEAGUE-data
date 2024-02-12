# Generated by Django 5.0.1 on 2024-02-12 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_organization'),
        ('rounds', '0002_drawnround'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuuro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuuro_number', models.IntegerField(verbose_name='fuuro number')),
                ('fuuro_type', models.CharField(choices=[('CHI', 'チー'), ('PON', 'ポン'), ('KAN', 'カン'), ('MINKAN', '明槓'), ('KAKAN', '加槓'), ('ANKAN', '暗槓')], max_length=255, verbose_name='fuuro type')),
                ('fuuro_hands', models.CharField(max_length=255, verbose_name='fuuro hands')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rounds.round')),
            ],
        ),
    ]