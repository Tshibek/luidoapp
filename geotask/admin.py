from django.contrib import admin
from . import models


# Register your models here.
class ProjectClient(admin.TabularInline):
    model = models.Project
    can_delete = True


class CustomClientAdmin(admin.ModelAdmin):
    inlines = (ProjectClient,)


admin.site.register(models.Client, CustomClientAdmin)
admin.site.register(models.Task)
admin.site.register(models.StatusTask)



