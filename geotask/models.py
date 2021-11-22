from django.contrib.auth.models import User
from django.db import models

from core.models import Team
from geotask import utils


class Client(models.Model):
    order_number = models.PositiveSmallIntegerField()
    last_name = models.CharField(max_length=120)


class ImageTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(choices=utils.TYPE, max_length=40)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ManyToManyField(ImageTask)


class Comment(models.Model):
    task = models.ForeignKey(Task, models.CASCADE)
    comment = models.TextField()


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    file = models.FileField()


class StatusTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=utils.STATUS)
