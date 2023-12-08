from django.db import models

# Create your models here.
# Основные параметры
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )
    descriptions = models.TextField(
        max_length=500,
        verbose_name='Описание',
        blank=True,null=True
    )
    image = models.ImageField(
        upload_to='banner_iamages',
        verbose_name='Фото',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Настройки баннера'
        verbose_name_plural = 'Настройка баннера'

# ИСТОРИЯ СОЗДАНИЯ
class HistoryCreated(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        blank=True,null=True
    )
    iamge = models.ImageField(
        upload_to='created_history_imaes',
        verbose_name='Фото',
        blank=True,null=True
    )
    def __str__(self) -> str:
        return self.text
    class Meta:
        verbose_name = 'Истории создание'
        verbose_name_plural = 'История создание'

#НАШИ ЦЕННОСТИ
class OurValues(models.Model):
    image = models.ImageField(
        upload_to='ourvalues_images/',
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

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Наши ценности'
        verbose_name_plural = 'Наш сенност'

# ПРИНЦИПЫ РАБОТЫ
class Principles_work(models.Model):
    image = models.ImageField(
        upload_to='principleswork_images/',
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
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Принципы работы'
        verbose_name_plural = 'Принцип работы'

# НАША КОМАНДА
class Team(models.Model):
    iamge = models.ImageField(
        upload_to='team_images/',
        verbose_name='Фото',
        blank=True,null=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        blank=True,null=True
    )
    job = models.CharField(
        max_length=255,
        verbose_name='Звание',
        blank=True,null=True
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Наши коаманда'
        verbose_name_plural = 'Команда'
        
