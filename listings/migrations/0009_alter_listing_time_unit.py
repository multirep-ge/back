# Generated by Django 5.0.1 on 2024-02-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_listing_time_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='time_unit',
            field=models.CharField(choices=[('საათში', 'hour'), ('თვეში', 'month')], default='hour', max_length=10),
        ),
    ]
