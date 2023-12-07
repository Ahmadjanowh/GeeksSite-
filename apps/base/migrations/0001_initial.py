# Generated by Django 5.0 on 2023-12-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bishkek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoene', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номмер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная Почта')),
                ('addres_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('addres_map', models.URLField(blank=True, null=True, verbose_name='Сылка на дарес в карте')),
            ],
            options={
                'verbose_name': 'Контактный данные Бишкек',
                'verbose_name_plural': 'Контактный данный Бишкек',
            },
        ),
        migrations.CreateModel(
            name='CoursesIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses_images/', verbose_name='Курсы для главного')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='KaraBalta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoene', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номмер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная Почта')),
                ('addres_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('addres_map', models.URLField(blank=True, null=True, verbose_name='Сылка на дарес в карте')),
            ],
            options={
                'verbose_name': 'Контактный данные Кара-Балта',
                'verbose_name_plural': 'Контактный данный Кара-балта',
            },
        ),
        migrations.CreateModel(
            name='Osh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoene', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номмер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная Почта')),
                ('addres_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('addres_map', models.URLField(blank=True, null=True, verbose_name='Сылка на дарес в карте')),
            ],
            options={
                'verbose_name': 'Контактный данные ОШ',
                'verbose_name_plural': 'Контактный данный ОШ',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок сайта')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_images/', verbose_name='Логотип сайта')),
                ('header_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Загаловок header части')),
                ('header_descriptions', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание header части')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Сылка на телеграм')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Сылка на ютуб')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Сылка на инстаграм')),
                ('watsapp', models.URLField(blank=True, null=True, verbose_name='Сылка на ватсап')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Сылка на линкедин')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Сылка на фейсбук')),
                ('tiktok', models.URLField(blank=True, null=True, verbose_name='Сылка на тикток')),
            ],
            options={
                'verbose_name': 'Основные настройки',
                'verbose_name_plural': 'Основной настройка',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iamge', models.ImageField(blank=True, null=True, upload_to='student_images/', verbose_name='Наши выпусник')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия имя')),
                ('job', models.CharField(blank=True, max_length=255, null=True, verbose_name='Направление / место работы')),
            ],
        ),
    ]