# Generated by Django 3.1 on 2021-12-21 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0005_auto_20211221_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='court_id',
            new_name='court',
        ),
    ]