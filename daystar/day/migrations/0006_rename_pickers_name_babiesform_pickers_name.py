# Generated by Django 4.2.11 on 2024-04-25 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0005_rename_name_of_the_person_that_has_taken_a_child_babiesform_pickers_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='babiesform',
            old_name='Pickers_name',
            new_name='pickers_name',
        ),
    ]
