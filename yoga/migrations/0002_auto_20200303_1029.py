# Generated by Django 2.2.6 on 2020-03-03 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='Title',
            new_name='title',
        ),
    ]
