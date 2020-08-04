# Generated by Django 3.0.9 on 2020-08-04 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200804_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.FileField(blank=True, upload_to='home/storeimages'),
        ),
    ]