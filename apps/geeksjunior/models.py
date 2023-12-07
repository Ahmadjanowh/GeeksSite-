from django.db import models

# Create your models here.
#Основные параметры 
class Settings(models.Model):
    banner_title = models.CharField(
        max_length=255,
        verbose_name='Баннер загаловок',
        blank=True,null=True
    )
    banner_descriptions = models.TextField(
        max_length=500,
        verbose_name='Баннер описание',
        blank=True,null=True
    )
    banner_image = models.ImageField(
        upload_to='banner_photo',
        verbose_name='Баннер описание',
        blank=True,null=True
    )

# Статистика
class Statistic(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True,null=True
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True,null=True
    )

# ПОЧЕМУ СТОИТ ВЫБРАТЬ GEEKS JUNIOR
class HowJunior(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
        blank=True,null=True
    )

# Курсы GeeksJunior
class GeekaJuniorCourses(models.Model):
    iamge = models.ImageField(
        upload_to='geeksjunior_images',
        verbose_name='Фотография',
        blank=True,null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        blank=True,null=True
    )
    start = models.CharField(
        max_length=255,
        verbose_name='Старт',
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
        blank=True,null=True
    )
    moth = models.CharField(
        max_length=255,
        verbose_name='Делительность',
        blank=True,null=True
    )

# ПОСЕТИТЕ БЕСПЛАТНЫЙ УРОК И ПОЛУЧИТЕ СКИДКУ
class FreLesson(models.Model):
    image  = models.ImageField(
        upload_to='freelesson_images/',
        verbose_name='Фото',
        blank=True,null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
        blank=True,null=True
    )
    