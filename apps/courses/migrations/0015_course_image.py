# Generated by Django 5.0 on 2023-12-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_rename_larning_img_learning_learning_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=1, upload_to='course_images/', verbose_name='Изоображение курса'),
            preserve_default=False,
        ),
    ]
