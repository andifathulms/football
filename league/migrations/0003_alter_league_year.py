# Generated by Django 3.2.9 on 2021-12-06 05:43

import django.core.validators
from django.db import migrations, models
import league.models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20211206_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1850), league.models.max_value_current_year], verbose_name='year'),
        ),
    ]
