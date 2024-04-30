# Generated by Django 5.0.4 on 2024-04-30 12:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Babiesform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_baby', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('parents_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('babys_number', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category_doll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorystay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitterform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
                ('location', models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('next_of_kin', models.CharField(max_length=200)),
                ('national_identification_number', models.CharField(max_length=200)),
                ('recommenders_name', models.CharField(max_length=200)),
                ('religon', models.CharField(blank=True, max_length=200, null=True)),
                ('level_of_education', models.CharField(choices=[('diploma', 'Diploma'), ('highschool certificate', 'Highschool certificate'), ('others', 'Others')], max_length=200)),
                ('sitter_number', models.IntegerField(default=0)),
                ('contacts', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baby_number', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('timein', models.TimeField()),
                ('care_taker', models.CharField(max_length=200)),
                ('baby_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
            ],
        ),
        migrations.AddField(
            model_name='babiesform',
            name='c_stay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='day.categorystay'),
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baby_number', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('timeout', models.TimeField()),
                ('pickers_name', models.CharField(max_length=200)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('babys_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
            ],
        ),
        migrations.CreateModel(
            name='Doll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_doll', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('issued_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('received_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('Unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('c_doll', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.category_doll')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('payno', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='ugx', max_length=10, null=True)),
                ('c_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.categorystay')),
                ('payee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
            ],
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('Unit_price', models.IntegerField(null=True)),
                ('received_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.category')),
            ],
        ),
        migrations.CreateModel(
            name='Salesrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.IntegerField(default=0)),
                ('amount_received', models.IntegerField(default=0)),
                ('sale_date', models.DateField(default=django.utils.timezone.now)),
                ('unit_price', models.IntegerField(default=0)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.doll')),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
            ],
        ),
        migrations.CreateModel(
            name='Sitter_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitter_number', models.IntegerField(default=0)),
                ('date_of_arrival', models.DateField(default=django.utils.timezone.now)),
                ('timein', models.TimeField()),
                ('Attendancestatus', models.CharField(choices=[('onduty', 'onduty')], max_length=100)),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitterform')),
            ],
        ),
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('day', models.CharField(choices=[('fullday', 'fullday'), ('halfday', 'halfday')], max_length=100)),
                ('baby_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitterform')),
            ],
        ),
        migrations.CreateModel(
            name='Usedlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_issued', models.IntegerField(default=0)),
                ('usage_date', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.procurement')),
            ],
        ),
    ]
