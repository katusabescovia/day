# Generated by Django 5.0.4 on 2024-05-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0004_remove_departure_date_remove_departure_timeout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babiesform',
            name='arrival_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='departure',
            name='date_of_departure',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sitter_departure',
            name='date_of_departure',
            field=models.DateTimeField(),
        ),
    ]
