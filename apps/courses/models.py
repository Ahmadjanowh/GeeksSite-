from django.db import models

class Course(models.Model):
    image = models.ImageField(
        upload_to='course_images/',
        verbose_name='Изоображение курса'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        blank=True,null=True
    )
    start = models.CharField(
        max_length=255,
        verbose_name='Старт курса',
        blank=True,null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,null=True
    )
    moth = models.CharField(
        max_length=255,
        verbose_name='Делителность',
        blank=True,null=True
    )
    price = models.CharField(
        verbose_name='Цена',
        max_length=255,
        blank=True,null=True
    )
    lessons = models.CharField(
        max_length=255,
        verbose_name='Уроки',
        blank=True,null=True
    )
    techers = models.CharField(
        max_length=255,
        verbose_name='Переподаватели',
        null=True,blank=True
    )
    time = models.CharField(
        max_length=255,
        verbose_name='Время',
        blank=True,null=True
    )
    graphics = models.CharField(
        max_length=255,
        verbose_name='График',
        blank=True,null=True
    )
    banner_description = models.CharField(
        max_length=255,
        verbose_name='Баннер описание',
        blank=True,null=True
    )
    about_course1 = models.TextField(
        verbose_name='Подроне о курса 1',
        blank=True,null=True
    )
    about_course2 = models.TextField(
        verbose_name='Подроне о курса 1',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Добавить курс',
        verbose_name_plural = 'Добавить курс'

class Learning(models.Model):
    frg_key = models.ForeignKey(Course,on_delete=models.CASCADE)
    learning_img = models.ImageField(
        upload_to='course_images/',
        verbose_name='Фото что изучет',
    )
    learning_title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    def __str__(self) -> str:
        return self.learning_title
    
    class Meta:
        verbose_name = 'Что изучает',
        verbose_name_plural = 'Что изучает'