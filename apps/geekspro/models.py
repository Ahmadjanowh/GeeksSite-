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

    def __str__(self) -> str:
        return self.banner_title
    
    class Meta:
        verbose_name = 'Настройки беннера'
        verbose_name_plural = 'Натройка баннера'

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

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = 'Статистики'
        verbose_name_plural = 'Статистика'

# Почему GeeksPro
class HowGeeksPro(models.Model):
    title = models.TextField(
        max_length=800,
        verbose_name='Почему именно GeeksPro'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Почему Geekspro'
        verbose_name_plural = 'Почему Geekspro'

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

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Вопросы ответы'
        verbose_name_plural = 'Вопросы ответы'

# Парнеры
class Partners(models.Model):
    link = models.URLField(
        verbose_name='Сылка',
        blank=True,null=True
    )
    image = models.ImageField(
        upload_to='partner_images/',
        verbose_name='Фото',
        blank=True,null=True
    )

    class Meta:
        verbose_name = 'Партеры'
        verbose_name_plural = 'Парноры'
        
    
    