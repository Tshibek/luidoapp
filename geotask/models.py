from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from core.models import Team
from geotask import utils


# TODO ADD INLINE CREATE TASK WITH STATUS

class Client(models.Model):
    order_number = models.PositiveSmallIntegerField()
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return self.order_number


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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.client.order_number} type {self.type} team {self.team.team} date {self.date} "

    def project(self):
        project = Project.objects.filter(client=self.client).all()
        return project


class Comment(models.Model):
    task = models.ForeignKey(Task, models.CASCADE)
    comment = models.TextField(editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"order {self.task.client.order_number} comment {self.comment}"


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    file = models.FileField(null=True,
                            blank=True,
                            validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return f"PDF FOR {self.client.order_number}"


class StatusTask(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=utils.STATUS, default='Zaakceptowane')

    def __str__(self):
        return f"Order {self.task.client.order_number} Status - {self.status }"
