# Generated by Django 4.1 on 2022-09-10 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_alter_tournamentmodel_type_of_tornament'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournamentmodel',
            options={'verbose_name': 'Турнир', 'verbose_name_plural': 'Турниры'},
        ),
    ]
