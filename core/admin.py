from django.contrib import admin
from . import models
from django.contrib import admin
from video_encoding.admin import FormatInline
from .models import MontageVideoGallery


class GalleryMontagePaid(admin.TabularInline):
    model = models.MontageGallery
    can_delete = True


class CustomMontagePaidAdmin(admin.ModelAdmin):
    inlines = (GalleryMontagePaid,)


class DailyMontageAdmin(admin.ModelAdmin):
    ordering = ['-date']


@admin.register(MontageVideoGallery)
class VideoAdmin(admin.ModelAdmin):
    inlines = (FormatInline,)

    list_dispaly = ('get_filename', 'width', 'height', 'duration')
    fields = ('file', 'width', 'height', 'duration')
    readonly_fields = fields


@admin.register(models.MonterDaily)
class MonterDailyAdmin(admin.ModelAdmin):
    model = models.MonterDaily
    list_display = ['name_monter', 'status', 'time_start', 'end_time', 'daily_hours', 'date']
    list_filter = ('status', 'date', 'time_start', 'end_time', 'daily_hours')
    search_fields = ['name_monter']
    @admin.display(description='Monter name', ordering='name__name')
    def name_monter(self, obj):
        return obj.name.name


admin.site.register(models.Monter)
admin.site.register(models.Team)
admin.site.register(models.DailyMontage, DailyMontageAdmin)

admin.site.register(models.MontagePaid, CustomMontagePaidAdmin)
