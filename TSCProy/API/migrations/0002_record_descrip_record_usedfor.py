# Generated by Django 4.1.4 on 2022-12-25 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='descrip',
            field=models.CharField(default='No description', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='usedFor',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 25, 19, 14, 25, 385162, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
