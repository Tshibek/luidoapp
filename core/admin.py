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
    list_display = ['montage_team', 'montage_type', 'status', 'date', 'paid', ]
    list_filter = ('status', 'days', 'date')
    raw_id_fields = ('montage',)
    search_fields = ['montage__team_team', ]

    @admin.display(description='montage team name', ordering='montage__team')
    def montage_team(self, obj):
        return obj.montage.team.team

    @admin.display(description='Montage type', ordering='montage__type')
    def montage_type(self, obj):
        return obj.montage.type


class DailyMontageAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ['montage_team', 'type', 'date']
    list_filter = ('type', 'team__team' 'date')
    raw_id_fields = ('team',)
    search_fields = ['team_team', ]

    @admin.display(description='montage team name', ordering='team__team')
    def montage_team(self, obj):
        return obj.team.team


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
    list_filter = ('status', 'date',)
    raw_id_fields = ('name',)
    search_fields = ['name__name', ]

    @admin.display(description='Monter name', ordering='name__name')
    def name_monter(self, obj):
        return obj.name.name


admin.site.register(models.Monter)
admin.site.register(models.Team)
admin.site.register(models.DailyMontage, DailyMontageAdmin)

admin.site.register(models.MontagePaid, CustomMontagePaidAdmin)
