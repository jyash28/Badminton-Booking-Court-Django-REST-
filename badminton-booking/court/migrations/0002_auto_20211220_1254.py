# Generated by Django 3.1 on 2021-12-20 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddCourt',
            new_name='Court',
        ),
    ]