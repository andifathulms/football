# Generated by Django 3.2.9 on 2021-12-06 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='chairman',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='team',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.country'),
        ),
        migrations.AlterField(
            model_name='team',
            name='owner',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
