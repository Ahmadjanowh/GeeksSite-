# Generated by Django 5.0 on 2023-12-08 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_phoene_karabalta_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='osh',
            old_name='phoene',
            new_name='phone',
        ),
    ]