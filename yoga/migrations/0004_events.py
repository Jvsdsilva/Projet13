# Generated by Django 2.2.6 on 2020-03-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0003_auto_20200303_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=3000)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='default.jpg', upload_to='')),
            ],
        ),
    ]
