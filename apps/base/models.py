from django.db import models

# Create your models here.
# На все модельки дан парметр  blank=True,null=True чтобы админ панель был более гипким 

class Settings(models.Model):
    # Мадельки для header части
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта',
        blank=True,null=True 
    )
    logo = models.ImageField(
        upload_to='logo_images/',
        verbose_name='Логотип сайта',
        blank=True,null=True
    )
    header_title = models.CharField(
        max_length=255,
        verbose_name='Загаловок header части',
        blank=True,null=True
    )
    header_descriptions = models.TextField(
        max_length=500,
        verbose_name='Описание header части',
        blank=True,null=True
    )  
  
    # Социальные сети
    telegram = models.URLField(
        verbose_name='Сылка на телеграм',
        blank=True,null=True
    )
    youtube = models.URLField(
        verbose_name='Сылка на ютуб',
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name='Сылка на инстаграм',
        blank=True,null=True
    )
    watsapp= models.URLField(
        verbose_name='Сылка на ватсап',
        blank=True,null=True
    )
    linkedin = models.URLField(
        verbose_name='Сылка на линкедин',
        blank=True,null=True
    )
    facebook = models.URLField(
        verbose_name='Сылка на фейсбук',
        blank=True,null=True
    )
    tiktok = models.URLField(
        verbose_name='Сылка на тикток',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.title, self.header_title
    
    class Meta:
        verbose_name = 'Основные настройки'
        verbose_name_plural = 'Основной настройка'

# Кем ты можеж стать после курса 
class HowAreYou(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )
    descriptions = models.TextField(
        max_length=800,
        verbose_name='Описание',
        blank=True,null=True
    )
    def __str__(self) -> str:
        return self.title, self.descriptions
    
    class Meta:
        verbose_name = 'Кем ты можеш стать после курса'
        verbose_name_plural = 'Кем ты сожеш стать после курса'

# ПОЧЕМУ СТОИТЬ УЧИТЬСЯ В GEEKS ?
class LearningGeeks(models.Model):
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
        return self.title, self.descriptions
    
    class Meta:
        verbose_name = 'Почему стоить учиться в Geeks ?'
        verbose_name_plural = 'Почему стоить учиться в Geeks ?'

#   GEEKS В ЦИФРАХ
class GeeksInt(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True,null=True
    )
    def __str__(self) -> str:
        return self.title, self.descriptions
    
    class Meta:
        verbose_name = 'Geek в цифрах'
        verbose_name_plural = 'Geeks в цифрах'

# GEEKS ONLINE
class GeeksOnline(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        blank=True,null=True
    )  
    descriptions = models.TextField(
        verbose_name='Описание',
        blank=True,null=True
    )  
    image = models.ImageField(
        upload_to='geeksonline_images/',
        verbose_name='Фотография',
        blank=True,null=True
    )
    link = models.URLField(
        verbose_name='Сылка на страницу',
        blank=True,null=True
    )
    def __str__(self) -> str:
        return self.title, self.descriptions
    
    class Meta:
        verbose_name = 'Geek Онлайн'
        verbose_name_plural = 'Geeks Онлайн'

# КУРСЫ ПРОГРАММИРОВАНИЯ БИШКЕК (ИСТОРИЯ GEEKS)
class GeeksHistory(models.Model):
    image_1 = models.ImageField(
        upload_to='history_images/',
        verbose_name='Первое фото',
        blank=True,null=True
    )
    image_2 = models.ImageField(
        upload_to='history_images/',
        verbose_name='Второе фото',
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
        return self.title, self.descriptions
    
    class Meta:
        verbose_name = 'История Geeks'
        verbose_name_plural = 'История Geeks'

# Курсы для главного 
class CoursesIndex(models.Model):
    image = models.ImageField(
        upload_to='courses_images/',
        verbose_name='Курсы для главного',
        blank=True,null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        blank=True,null=True
    )
    def __str__(self) -> str:
        return self.title, self.descriptions
    
    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курс'
    

# Наши выпусники
class Students(models.Model):
    iamge = models.ImageField(
        upload_to='student_images/',
        verbose_name='Наши выпусник',
        blank=True,null=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Фамилия имя',
        blank=True,null=True
    )
    job = models.CharField(
        max_length=255,
        verbose_name='Направление / место работы',
        blank=True,null=True
    )
    def __str__(self) -> str:
        return self.title, self.descriptions
    
    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студент'
 
# Контактные информатции филиалов 
# Бишкек
class Bishkek(models.Model):
    phoene = models.CharField(
        max_length=255,
        verbose_name='Номмер телефона',
        blank=True,null=True
    )
    email = models.EmailField(
        verbose_name='Электронная Почта',
        blank=True,null=True
    )
    addres_text = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True,null=True
    )
    addres_map = models.URLField(
        verbose_name='Сылка на дарес в карте',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.email, self.addres_text
    
    class Meta:
        verbose_name = 'Контактный данные Бишкек'
        verbose_name_plural = 'Контактный данный Бишкек'

# ОШ
class Osh(models.Model):
    phoene = models.CharField(
        max_length=255,
        verbose_name='Номмер телефона',
        blank=True,null=True
    )
    email = models.EmailField(
        verbose_name='Электронная Почта',
        blank=True,null=True
    )
    addres_text = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True,null=True
    )
    addres_map = models.URLField(
        verbose_name='Сылка на дарес в карте',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.email, self.addres_text
    
    class Meta:
        verbose_name = 'Контактный данные ОШ'
        verbose_name_plural = 'Контактный данный ОШ'

# Кара-Балта
class KaraBalta(models.Model):
    phoene = models.CharField(
        max_length=255,
        verbose_name='Номмер телефона',
        blank=True,null=True
    )
    email = models.EmailField(
        verbose_name='Электронная Почта',
        blank=True,null=True
    )
    addres_text = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True,null=True
    )
    addres_map = models.URLField(
        verbose_name='Сылка на дарес в карте',
        blank=True,null=True
    )

    def __str__(self) -> str:
        return self.email, self.addres_text
    
    class Meta:
        verbose_name = 'Контактный данные Кара-Балта'
        verbose_name_plural = 'Контактный данный Кара-балта'

# Выпускние работы студентов
class StudentsProject(models.Model):
    image = models.ImageField(
        upload_to='student_project_images/',
        verbose_name='Выаускные работы студентов',
        blank=True,null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        blank=True,null=True
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True,null=True
    )
    link = models.URLField(
        verbose_name='Сылка на проект',
        blank=True,null=True
    )

