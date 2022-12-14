# Generated by Django 3.2.16 on 2023-01-04 11:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(max_length=10)),
                ('bathrooms', models.FloatField(default=0.0)),
                ('bedrooms', models.IntegerField(default=0)),
                ('home_size', models.CharField(max_length=50)),
                ('last_sold_date', models.DateField(blank=True, default=datetime.datetime(2023, 1, 4, 11, 13, 41, 271887, tzinfo=utc))),
                ('last_sold_price', models.IntegerField(blank=True, default=0)),
                ('link', models.URLField()),
                ('price', models.IntegerField(default=0)),
                ('property_size', models.IntegerField(default=0)),
                ('rent_price', models.IntegerField(blank=True)),
                ('rentzestimate_amount', models.IntegerField(default=0)),
                ('rentzestimate_last_updated', models.DateField(default=datetime.datetime(2023, 1, 4, 11, 13, 41, 271922, tzinfo=utc))),
                ('tax_value', models.FloatField(default=0.0)),
                ('tax_year', models.IntegerField(default=0)),
                ('year_built', models.IntegerField(default=0)),
                ('zestimate_amount', models.IntegerField(default=0)),
                ('zestimate_last_updated', models.DateField(default=datetime.datetime(2023, 1, 4, 11, 13, 41, 271939, tzinfo=utc))),
                ('zillow_id', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('sate', models.CharField(max_length=3)),
                ('zipcode', models.IntegerField(default=0)),
            ],
        ),
    ]
