# Generated by Django 2.2.3 on 2019-07-17 08:36

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_auto_20190717_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='votes_total',
            field=models.IntegerField(default=0, verbose_name=django.contrib.auth.models.User),
        ),
    ]
