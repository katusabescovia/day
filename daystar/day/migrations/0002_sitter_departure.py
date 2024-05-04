# Generated by Django 5.0.4 on 2024-05-03 08:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitter_departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitter_number', models.IntegerField(default=0)),
                ('date_of_departure', models.DateField(default=django.utils.timezone.now)),
                ('timeout', models.TimeField()),
                ('sitters_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitter_arrival')),
            ],
        ),
    ]
