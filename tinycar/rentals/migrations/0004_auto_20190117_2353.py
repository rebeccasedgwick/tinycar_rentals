# Generated by Django 2.1.5 on 2019-01-17 23:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_booking_duration_hrs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='model',
            new_name='car',
        ),
        migrations.AlterField(
            model_name='booking',
            name='duration_hrs',
            field=models.IntegerField(default=1, help_text='Rental duration in hours', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Duration'),
        ),
    ]
