from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listing_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='_score',
            field=models.IntegerField(default=0),

        ),
    ]
