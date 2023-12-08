from django.contrib import admin
from apps.courses.models import *

# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

@admin.register(Tehnalogis)
class TehnalogisAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)
