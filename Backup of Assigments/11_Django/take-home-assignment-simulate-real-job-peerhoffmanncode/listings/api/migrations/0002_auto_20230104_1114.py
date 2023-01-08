# Generated by Django 3.2.16 on 2023-01-04 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='last_sold_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='houses',
            name='rentzestimate_last_updated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='houses',
            name='zestimate_last_updated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]