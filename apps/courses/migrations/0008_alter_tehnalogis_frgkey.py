# Generated by Django 5.0 on 2023-12-10 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_cours_frkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tehnalogis',
            name='frgkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses'),
        ),
    ]