from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Monter)
admin.site.register(models.Team)
admin.site.register(models.DailyMontage)
admin.site.register(models.MonterDaily)
admin.site.register(models.MontagePaid)
