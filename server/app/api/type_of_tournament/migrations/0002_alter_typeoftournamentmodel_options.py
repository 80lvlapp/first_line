# Generated by Django 4.1 on 2022-09-10 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type_of_tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeoftournamentmodel',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Типы турниров'},
        ),
    ]
