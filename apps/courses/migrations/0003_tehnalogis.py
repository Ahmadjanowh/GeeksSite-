# Generated by Django 5.0 on 2023-12-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_cours_options_alter_courses_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tehnalogis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Загаловок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses_iamges', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Что изучет',
                'verbose_name_plural': 'Что изучет',
            },
        ),
    ]
