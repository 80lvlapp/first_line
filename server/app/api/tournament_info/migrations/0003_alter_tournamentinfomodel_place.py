# Generated by Django 4.1 on 2022-11-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_info', '0002_alter_tournamentinfomodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentinfomodel',
            name='place',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
