# Generated by Django 3.2.16 on 2023-01-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_sate_houses_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='home_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='houses',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
