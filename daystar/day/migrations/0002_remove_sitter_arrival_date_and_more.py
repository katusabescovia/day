# Generated by Django 4.2.11 on 2024-04-28 09:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitter_arrival',
            name='date',
        ),
        migrations.AlterField(
            model_name='sitter_arrival',
            name='Attendancestatus',
            field=models.CharField(choices=[('onduty', 'onduty')], max_length=100),
        ),
        migrations.AlterField(
            model_name='sitter_arrival',
            name='date_of_arrival',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sitterform',
            name='religon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baby_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitterform')),
            ],
        ),
    ]