from django.contrib import admin
from apps.geekspro.models import *
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('banner_title',)
    search_fields =  ('banner_title',)

@admin.register(StatisticGeekspro)
class StatisticGeeksProAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(HowGeeksPro)
class HowGeeksCoursesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(GeeksproFAQ)
class GeeksProFAQAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =  ('title',)

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('link',)
    search_fields =  ('link',)
