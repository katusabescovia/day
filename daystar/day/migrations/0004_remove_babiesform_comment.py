# Generated by Django 4.2.11 on 2024-04-25 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0003_babiesform_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babiesform',
            name='comment',
        ),
    ]
