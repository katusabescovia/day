# Generated by Django 5.0.4 on 2024-04-16 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('payno', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='ugx', max_length=10, null=True)),
                ('c_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.category_stay')),
            ],
        ),
        migrations.CreateModel(
            name='Babiesform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_baby', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('age', models.IntegerField(default=0)),
                ('parents_name', models.CharField(blank=True, max_length=200, null=True)),
                ('name_of_the_person_brought_by_the_baby', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('babys_number', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('timein', models.DateTimeField(blank=True, null=True)),
                ('timeout', models.DateTimeField(blank=True, null=True)),
                ('c_stay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.category_stay')),
                ('c_fees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.payment')),
            ],
        ),
    ]
