from django.db import models

# Create your models here.
# ДЛя основных курсов 
class CoursPost(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Электронная Почта'
    )
    cours = models.CharField(
        max_length=255,
        verbose_name='Выбирал курс'
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Записи на курсов'
        verbose_name_plural = 'Запись на курс'

class SelectCourses(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        verbose_name = 'Курсы на выбор'
        verbose_name_plural = 'Курс на выбор'

# Для курсов GeeksJunior 
class GeeksJuniorCoursPost(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Электронная Почта'
    )
    cours = models.CharField(
        max_length=255,
        verbose_name='Выбирал курс'
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Записи на курсов Geeks Junior'
        verbose_name_plural = 'Запись на курс Geeks Junior'

class JuniorSelectCourses(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        verbose_name = 'Курсы на выбор Junior'
        verbose_name_plural = 'Курс на выбор Junior'

# Для заявки в Geeks Pro 
class GeeksProPost(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Электронная Почта'
    )
    direction = models.CharField(
        max_length=255,
        verbose_name='Направление'
    )
    learning = models.CharField(
        max_length=255,
        verbose_name='Где училься'
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Заявки на Geeks Pro'
        verbose_name_plural = 'Заявка на Geeks Pro'

class GeeksProdirections(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        verbose_name = 'Выбор направлении на Geeks Pro'
        verbose_name_plural = 'Направление на Geeks Pro'