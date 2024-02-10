# Generated by Django 5.0.1 on 2024-02-10 18:10

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_georgian_alphabet', message='მიუთითეთ მხოლოდ ქართული ასოები', regex='^[ა-ჰ\\s]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_georgian_alphabet', message='მიუთითეთ მხოლოდ ქართული ასოები', regex='^[ა-ჰ\\s]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_georgian_alphabet', message='მიუთითეთ მხოლოდ ქართული ასოები', regex='^[ა-ჰ\\s]+$')])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.city')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to='images/listing')),
                ('views', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.city')),
                ('currency', models.ForeignKey(default='₾', on_delete=django.db.models.deletion.CASCADE, to='listings.currency')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.district')),
            ],
        ),
    ]
