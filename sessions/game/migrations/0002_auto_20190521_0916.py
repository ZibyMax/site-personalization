# Generated by Django 2.1.1 on 2019-05-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='value_found',
            new_name='is_value_found',
        ),
        migrations.AlterField(
            model_name='game',
            name='current_attempt',
            field=models.IntegerField(default=0),
        ),
    ]
