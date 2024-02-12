# Generated by Django 5.0.1 on 2024-02-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_listing__score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
