# Generated by Django 3.1.3 on 2020-12-21 21:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20201221_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 21, 41, 34, 722705, tzinfo=utc)),
        ),
    ]
