# Generated by Django 2.2.6 on 2020-03-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0004_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='thumb',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
