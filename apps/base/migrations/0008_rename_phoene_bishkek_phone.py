# Generated by Django 5.0 on 2023-12-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_phoene_osh_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bishkek',
            old_name='phoene',
            new_name='phone',
        ),
    ]
