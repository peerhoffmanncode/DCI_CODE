# Generated by Django 4.1.4 on 2022-12-14 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='due_date',
            new_name='creation_date',
        ),
    ]
