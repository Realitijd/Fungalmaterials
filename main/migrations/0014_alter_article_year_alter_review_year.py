# Generated by Django 4.2.16 on 2024-09-07 07:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_article_day_alter_article_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1850), django.core.validators.MaxValueValidator(2025)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1850), django.core.validators.MaxValueValidator(2025)]),
        ),
    ]
