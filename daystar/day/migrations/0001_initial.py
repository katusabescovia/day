# Generated by Django 5.0.4 on 2024-05-19 14:11

import day.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Sitter_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_arrival', models.DateTimeField()),
                ('Attendancestatus', models.CharField(choices=[('onduty', 'onduty')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitterform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('location', models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('next_of_kin', models.CharField(max_length=200)),
                ('national_identification_number', models.CharField(max_length=200, validators=[day.models.NINvalidate])),
                ('recommenders_name', models.CharField(max_length=200)),
                ('religon', models.CharField(blank=True, max_length=200, null=True)),
                ('level_of_education', models.CharField(choices=[('Diploma', 'Diploma'), ('Highschool certificate', 'Highschool certificate'), ('Others', 'Others')], max_length=200)),
                ('contacts', models.CharField(max_length=100, validators=[day.models.contactvalidate])),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Babiesform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_baby', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('parents_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('arrival_time', models.DateTimeField()),
                ('care_taker', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('c_stay', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='day.categorystay')),
                ('Assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitter_arrival')),
            ],
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_departure', models.DateTimeField(null=True)),
                ('pickers_name', models.CharField(max_length=200)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('babyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
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
                ('payment_type', models.CharField(choices=[('halfday', 'halfday'), ('fullday', 'fullday'), ('monthlyhalfday', 'monthlyhalfday'), ('monthlyfullfday', 'monthlyfullday')], max_length=100)),
                ('payno', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('actual_amount', models.IntegerField(choices=[(10000, '10000'), (15000, '15000'), (300000, '300000'), (450000, '450000')], default=0)),
                ('amount_paid', models.IntegerField(default=0)),
                ('Period_of_stay', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='day.categorystay')),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
            ],
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('Unit_price', models.IntegerField(null=True)),
                ('received_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.category')),
            ],
        ),
        migrations.CreateModel(
            name='Salesrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.IntegerField(blank=True, default=0, null=True)),
                ('amount_received', models.IntegerField(blank=True, default=0, null=True)),
                ('sale_date', models.DateField(default=django.utils.timezone.now)),
                ('unit_price', models.IntegerField(default=0)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.doll')),
                ('payee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.babiesform')),
            ],
        ),
        migrations.CreateModel(
            name='Sitter_departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_departure', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Offduty', 'Offduty')], max_length=100, null=True)),
                ('sitters_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitter_arrival')),
            ],
        ),
        migrations.AddField(
            model_name='sitter_arrival',
            name='sitter_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitterform'),
        ),
        migrations.CreateModel(
            name='Sitterpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField(default=3000)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('numbers_of_babies_attended_to', models.IntegerField(default=0)),
                ('sitter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day.sitter_arrival')),
            ],
        ),
        migrations.CreateModel(
            name='Usedlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_issued', models.IntegerField(blank=True, default=0, null=True)),
                ('usage_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='day.procurement')),
            ],
        ),
    ]
