# Generated by Django 5.0.1 on 2024-02-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_currency_delete_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]