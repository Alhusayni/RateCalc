# Generated by Django 4.2.3 on 2023-08-05 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlatRate', '0012_alter_calculator_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 5, 2, 12, 32, 145449, tzinfo=datetime.timezone.utc)),
        ),
    ]