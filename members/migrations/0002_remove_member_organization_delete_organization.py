# Generated by Django 5.0.1 on 2024-01-30 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='organization',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
