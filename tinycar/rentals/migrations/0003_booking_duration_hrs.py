# Generated by Django 2.1.5 on 2019-01-17 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='duration_hrs',
            field=models.IntegerField(default=1, help_text='Rental duration in hours', verbose_name='Duration'),
        ),
    ]
