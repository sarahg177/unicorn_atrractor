# Generated by Django 2.2.3 on 2019-07-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_ticket_votes_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='votes_total',
            field=models.IntegerField(default=0),
        ),
    ]
