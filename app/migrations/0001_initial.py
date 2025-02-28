# Generated by Django 5.1.6 on 2025-02-22 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('manzil', models.TextField()),
                ('tashkil_qilgan_sana', models.DateField()),
                ('fuqaro_soni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tavsiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=26)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EnergiyaSarfi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oy', models.CharField(choices=[('Yanvar', 'Yanvar'), ('Fevral', 'Fevral'), ('Mart', 'Mart'), ('Aprel', 'Aprel'), ('May', 'May'), ('Iyun', 'Iyun'), ('Iyul', 'Iyul'), ('Avgust', 'Avgust'), ('Sentabr', 'Sentabr'), ('Oktabr', 'Oktabr'), ('Noyabr', 'Noyabr'), ('Dekabr', 'Dekabr')], max_length=20)),
                ('yil', models.IntegerField()),
                ('elektr_kVt', models.FloatField()),
                ('gaz_m3', models.FloatField()),
                ('suv_m3', models.FloatField()),
                ('qoʻshilgan_vaqt', models.DateTimeField(auto_now_add=True)),
                ('mahalla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mahalla')),
            ],
        ),
    ]
