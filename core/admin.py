from django.contrib import admin
from . import models


class GalleryMontagePaid(admin.TabularInline):
    model = models.MontageGallery
    can_delete = True


class CustomMontagePaidAdmin(admin.ModelAdmin):
    inlines = (GalleryMontagePaid,)


admin.site.register(models.Monter)
admin.site.register(models.Team)
admin.site.register(models.DailyMontage)
admin.site.register(models.MonterDaily)
admin.site.register(models.MontagePaid, CustomMontagePaidAdmin)
