from django.db import models

# Create your models here.
# Все курсы
class Courses(models.Model):
    image = models.ImageField(
        upload_to='coureses_images/',
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
        verbose_name='Название курса',
        blank=True,null=True
    )
    descriptions = models.TextField(
        verbose_name='Опсание',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Добавить курс'
        verbose_name_plural = 'Добавить курс'

# Определонный курс
class Cours(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        blank=True,null=True
    )
    start = models.CharField(
        max_length=255,
        verbose_name='Старт',
        blank=True,null=True
    )
    time = models.CharField(
        max_length=255,
        verbose_name='Время',
        blank=True,null=True
    )
    graphik = models.CharField(
        max_length=255,
        verbose_name='График'
    )
    banner_descriptions = models.TextField(
        max_length=600,
        verbose_name='Баннер Описание',
        blank=True,null=True
    )
    moth = models.CharField(
        max_length=255,
        verbose_name='Длительность',
        blank=True,null=True
    )
    price = models.CharField(
        max_length=255,
        verbose_name='Цена',
        blank=True,null=True
    )
    lessons = models.CharField(
        max_length=255,
        verbose_name='Занятий',
        blank=True,null=True
    )
    teachers = models.CharField(
        max_length=255,
        verbose_name='Преподавателей'
    )
    descriptions = models.TextField(
        verbose_name='Описание курса',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Добробне о курса'
        verbose_name_plural = 'Подробне о курса'

class Tehnalogis(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )
    image = models.ImageField(
        upload_to='courses_iamges',
        verbose_name='Фотография',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Что изучет'
        verbose_name_plural = 'Что изучет'