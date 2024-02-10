# Generated by Django 5.0.1 on 2024-02-10 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_rename_winninghands_winninghand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='game',
        ),
        migrations.RemoveField(
            model_name='winninghand',
            name='round',
        ),
        migrations.RemoveField(
            model_name='winninghand',
            name='member',
        ),
        migrations.DeleteModel(
            name='HaiPai',
        ),
        migrations.DeleteModel(
            name='Round',
        ),
        migrations.DeleteModel(
            name='WinningHand',
        ),
    ]
