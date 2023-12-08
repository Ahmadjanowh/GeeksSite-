from django.contrib import admin
from apps.geeksjunior.models import *
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('banner_title',)
    search_fields = ('banner_title',)

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(HowJunior)
class HowjuniorAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(GeekaJuniorCourses)
class GeeksJuniorCoursesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(FreLesson)
class FreelessonAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)




