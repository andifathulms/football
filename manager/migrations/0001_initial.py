# Generated by Django 3.2.9 on 2021-12-06 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=100)),
                ('height', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerReign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='Manager', max_length=100)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.manager')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
