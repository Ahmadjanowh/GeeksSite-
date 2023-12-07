from django.db import models

# Create your models here.

class Settings(models.Model):
    banner_title = models.CharField(
        max_length=255,
        verbose_name='Баннер описание',
        blank=True,null=True
    )
    banner_descriptions = models.TextField(
        max_length=500,
        verbose_name='Бннер описание',
    )
    banner_image = models.ImageField(
        upload_to='banner_photos/',
        verbose_name='Баннер фото',
        blank=True,null=True
    )

# Статистика
class StatisticGeekspro(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )
    descriptions =models.TextField(
        max_length=500,
        verbose_name='Описание',
        blank=True,null=True
    )

# Почему GeeksPro
class HowGeeksPro(models.Model):
    title = models.TextField(
        max_length=800,
        verbose_name='Почему именно GeeksPro'
    )

# Попросы ответы
class GeeksproFAQ(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок' ,
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name='Описание',
        blank=True,null=True
    )

# Парнеры
class Partners(models.Model):
    link = models.URLField(
        verbose_name='Сылка',
        blank=True,null=True
    )
    iamge = models.ImageField(
        upload_to='partner_images/',
        verbose_name='Фото',
        blank=True,null=True
    )
    
    