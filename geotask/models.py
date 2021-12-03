import sys

from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from sorl.thumbnail import ImageField
from PIL import Image, ImageOps
from io import BytesIO
from core.models import Team, Monter
from geotask import utils


class Client(models.Model):
    order_number = models.PositiveSmallIntegerField()
    last_name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(str(self.order_number), self.last_name)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(choices=utils.TYPE, max_length=40)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    monters = models.ManyToManyField(Monter)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.client.order_number} type {self.type} team {self.team.team} date {self.date} "

    def project(self):
        project = Project.objects.filter(client=self.client).all()
        return project


def montage_gallery_path(instance, filename):
    today = timezone.localdate()
    today_path = today.strftime("%Y/%m/%d")
    return 'img/montage/{}/{}/{}'.format(today_path, instance.user.username, filename)


class TaskGallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    images = ImageField(upload_to=montage_gallery_path, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.images = self.compressImage(self.images)
        super(TaskGallery, self).save(*args, **kwargs)

    def compressImage(self, images):
        imageTemproary = Image.open(images)
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream, format='JPEG', quality=80)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % images.name.split('.')[0],
                                             'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage


class CommentTask(models.Model):
    task = models.ForeignKey(Task, models.CASCADE)
    comment = models.TextField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order {self.task.client.order_number} comment {self.comment}"


def projects_path(instance, filename):
    return 'pdf/projects/{}/{}'.format(instance.client.order_number, filename)


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    file = models.FileField(upload_to=projects_path,null=True,
                            blank=True,
                            validators=[FileExtensionValidator(['pdf'])])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PDF FOR {self.client.order_number}"


class StatusTask(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=utils.STATUS, default='Zaakceptowane')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.task.client.order_number} Status - {self.status}"

    @receiver(post_save, sender=Task)
    def update_task(sender, instance, created, **kwargs):
        if created:
            StatusTask.objects.create(task=instance)
        instance.statustask.save()
