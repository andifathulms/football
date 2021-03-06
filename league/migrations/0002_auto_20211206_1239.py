# Generated by Django 3.2.9 on 2021-12-06 05:39

import django.core.validators
from django.db import migrations, models
import league.models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='date_founded',
        ),
        migrations.AddField(
            model_name='league',
            name='year',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1984), league.models.max_value_current_year], verbose_name='year'),
            preserve_default=False,
        ),
    ]
