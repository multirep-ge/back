# Generated by Django 5.0.1 on 2024-02-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
