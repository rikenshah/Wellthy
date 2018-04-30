# Generated by Django 2.0.1 on 2018-04-26 15:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20180414_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthprofile',
            name='healthcare_costs',
            field=models.FloatField(blank=True, help_text='Enter your total healthcare costs (per year)', null=True, validators=[django.core.validators.MaxValueValidator(50000), django.core.validators.MinValueValidator(0)]),
        ),
    ]