# Generated by Django 5.0.1 on 2024-02-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_listing_time_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='time_unit',
            field=models.CharField(choices=[('საათში', 'hour'), ('თვეში', 'month')], default='საათში', max_length=10),
        ),
    ]
