from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(CoursPost)
class CoursPostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

@admin.register(SelectCourses)
class SelectCoursesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

@admin.register(GeeksJuniorCoursPost)
class GeeksJuniorCoursPostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

@admin.register(JuniorSelectCourses)
class juniorSelectCoursesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

@admin.register(GeeksProPost)
class GeeksProPostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

@admin.register(GeeksProdirections)
class GeeksprodrsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

