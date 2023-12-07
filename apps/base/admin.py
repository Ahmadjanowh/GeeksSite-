from django.contrib import admin
from apps.base.models import *

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title','header_title')
    search_fields = ('title','header_title')

@admin.register(CoursesIndex)
class CoursesIndexAdmin(admin.ModelAdmin):
    list_display = ('title','title')
    search_fields = ('title','title')

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name','job')
    search_fields = ('name','job')

@admin.register(Bishkek)
class BishkekAdmin(admin.ModelAdmin):
    list_display = ('email','addres_text')
    search_fields = ('email','addres_text')

@admin.register(Osh)
class OshAdmin(admin.ModelAdmin):
    list_display = ('email','addres_text')
    search_fields = ('email','addres_text')

@admin.register(KaraBalta)
class KaraBaltaAdmin(admin.ModelAdmin):
    list_display = ('email','addres_text')
    search_fields = ('email','addres_text')

@admin.register(HowAreYou)
class HowAreYourAdmin(admin.ModelAdmin):
    list_display = ('title','descriptions')
    search_fields = ('title','descriptions')

@admin.register(LearningGeeks)
class LearningGeeksAdmin(admin.ModelAdmin):
    list_display = ('title','descriptions')
    search_fields = ('title','descriptions')

@admin.register(GeeksInt)
class GeeksIntAdmin(admin.ModelAdmin):
    list_display = ('title','descriptions')
    search_fields = ('title','descriptions')

@admin.register(GeeksOnline)
class GeeksOnlineAdmin(admin.ModelAdmin):
    list_display = ('title','descriptions')
    search_fields = ('title','descriptions')

@admin.register(GeeksHistory)
class GeeksHistoryAdmin(admin.ModelAdmin):
    list_display = ('title','descriptions')
    search_fields = ('title','descriptions')





