# Generated by Django 5.0 on 2023-12-08 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_delete_geekshistory_alter_studentsproject_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karabalta',
            old_name='phoene',
            new_name='phone',
        ),
    ]
