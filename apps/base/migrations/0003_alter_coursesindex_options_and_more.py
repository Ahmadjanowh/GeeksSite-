# Generated by Django 5.0 on 2023-12-06 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_geekshistory_geeksint_geeksonline_howareyou_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursesindex',
            options={'verbose_name': 'Курсы', 'verbose_name_plural': 'Курс'},
        ),
        migrations.AlterModelOptions(
            name='geekshistory',
            options={'verbose_name': 'История Geeks', 'verbose_name_plural': 'История Geeks'},
        ),
        migrations.AlterModelOptions(
            name='geeksonline',
            options={'verbose_name': 'Geek Онлайн', 'verbose_name_plural': 'Geeks Онлайн'},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name': 'Студенты', 'verbose_name_plural': 'Студент'},
        ),
    ]
