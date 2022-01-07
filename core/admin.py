from django.contrib import admin
from django.utils.html import format_html

from . import models
from django.contrib import admin
from video_encoding.admin import FormatInline
from .models import MontageVideoGallery


class GalleryMontagePaid(admin.TabularInline):
    model = models.MontageGallery
    can_delete = True

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.images.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag']
    readonly_fields = ['image_tag']


class VideoAdmin(admin.TabularInline):
    model = models.MontageVideoGallery
    can_delete = True

    def video_tag(self, obj):
        return format_html(
            '<video controls="controls" width="200" height="200"><source src="{}"/></video>'.format(obj.file.url))

    video_tag.short_description = 'Video'

    list_display = ('get_filename', 'video_tag', 'width', 'height', 'duration')
    fields = ('file', 'width', 'height', 'duration', 'video_tag')
    readonly_fields = fields


class CustomMontagePaidAdmin(admin.ModelAdmin):
    inlines = (GalleryMontagePaid, VideoAdmin,)
    list_display = ['montage_team', 'montage_type', 'status', 'date', 'paid', ]
    list_filter = ('status', 'days', 'date')
    raw_id_fields = ('montage',)
    search_fields = ['montage__team_team', ]

    @admin.display(description='team name', ordering='montage__team')
    def montage_team(self, obj):
        return obj.montage.team.team

    @admin.display(description='Montage type', ordering='montage__type')
    def montage_type(self, obj):
        return obj.montage.type


class DailyMontageAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ['montage_team', 'type', 'date']
    list_filter = ('type', 'date')
    raw_id_fields = ('team',)
    search_fields = ['team__team', ]

    @admin.display(description='team name', ordering='team')
    def montage_team(self, obj):
        return obj.team.team


@admin.register(models.MonterDaily)
class MonterDailyAdmin(admin.ModelAdmin):
    model = models.MonterDaily
    list_display = ['montage_team','name_monter', 'status', 'time_start', 'end_time', 'daily_hours', 'date']
    list_filter = ('status', 'date',)
    raw_id_fields = ('name', 'daily_montage')
    search_fields = ['name__name', 'daily_montage__team__team']

    @admin.display(description='Monter name', ordering='name__name')
    def name_monter(self, obj):
        return obj.name.name

    @admin.display(description='Team name', ordering='daily_montage__team__team')
    def montage_team(self, obj):
        return obj.daily_montage.team.team


admin.site.register(models.Monter)
admin.site.register(models.Team)
admin.site.register(models.DailyMontage, DailyMontageAdmin)

admin.site.register(models.MontagePaid, CustomMontagePaidAdmin)
