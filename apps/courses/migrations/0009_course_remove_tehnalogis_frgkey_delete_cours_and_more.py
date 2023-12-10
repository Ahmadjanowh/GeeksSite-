# Generated by Django 5.0 on 2023-12-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_tehnalogis_frgkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('start', models.CharField(max_length=255, verbose_name='Старт курса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('time', models.CharField(max_length=255, verbose_name='Время')),
                ('graphics', models.CharField(max_length=255, verbose_name='График')),
                ('banner_description', models.CharField(max_length=255, verbose_name='Баннер описание')),
                ('about_course1', models.TextField(verbose_name='Подроне о курса 1')),
                ('about_course2', models.TextField(verbose_name='Подроне о курса 1')),
                ('larning_img', models.ImageField(upload_to='course_images/', verbose_name='Фото')),
                ('learning_title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': ('Что изучет',),
                'verbose_name_plural': 'Что изучет',
            },
        ),
        migrations.RemoveField(
            model_name='tehnalogis',
            name='frgkey',
        ),
        migrations.DeleteModel(
            name='Cours',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Tehnalogis',
        ),
    ]
