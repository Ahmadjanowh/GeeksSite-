# Generated by Django 5.0 on 2023-12-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=255, verbose_name='Электронная Почта')),
                ('cours', models.CharField(max_length=255, verbose_name='Выбирал курс')),
            ],
            options={
                'verbose_name': 'Записи на курсов',
                'verbose_name_plural': 'Запись на курс',
            },
        ),
        migrations.CreateModel(
            name='SelectCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Курсы на выбор',
                'verbose_name_plural': 'Курс на выбор',
            },
        ),
    ]