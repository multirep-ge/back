# Generated by Django 5.0.1 on 2024-02-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_teacher_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
