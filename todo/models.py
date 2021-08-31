from django.contrib.auth.models import User
from django.db import models
from . import utils


# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=utils.STATUS_TODO, max_length=30, default='ZGŁOSZONA')

