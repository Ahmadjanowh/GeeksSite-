from django.contrib import admin
from apps.courses.models import *

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ('learning_title',)
    search_fields = ('learning_title',)

