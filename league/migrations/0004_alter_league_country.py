# Generated by Django 3.2.9 on 2021-12-06 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
        ('league', '0003_alter_league_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.country'),
        ),
    ]
