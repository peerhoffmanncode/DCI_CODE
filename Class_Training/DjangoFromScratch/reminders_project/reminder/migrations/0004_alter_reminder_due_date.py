# Generated by Django 4.1.4 on 2022-12-14 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_reminder_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 14, 16, 46, 46, 295919)),
        ),
    ]
