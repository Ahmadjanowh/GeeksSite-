# Generated by Django 5.0 on 2023-12-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geekspro', '0002_alter_geeksprofaq_options_alter_howgeekspro_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geeksprofaq',
            options={'verbose_name': 'Вопросы ответы', 'verbose_name_plural': 'Вопросы ответы'},
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Партеры', 'verbose_name_plural': 'Парноры'},
        ),
        migrations.RenameField(
            model_name='partners',
            old_name='iamge',
            new_name='image',
        ),
    ]
