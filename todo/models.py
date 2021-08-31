from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from core.models import Team
from . import utils


# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(choices=utils.STATUS_TODO, max_length=30, default='ZGŁOSZONA')
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Todo, self).save(*args, **kwargs)
