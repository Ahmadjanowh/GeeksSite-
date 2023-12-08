from django.contrib import admin
from apps.about.models import *

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(HistoryCreated)
class HitoryCreatedAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields =  ('text',)

@admin.register(Principles_work)
class PrinciplesWorkAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields =  ('name',)

@admin.register(OurValues)
class OurValuesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)
