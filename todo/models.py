import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from core.models import Team
from . import utils


class StatusTodoQuerySet(models.QuerySet):
    def status_reported(self):
        return self.filter(status='ZGŁOSZONA')

    def status_contact(self):
        return self.filter(status='KONTAKT')

    def status_arranged(self):
        return self.filter(status='UMÓWIONA')

    def status_done(self):
        return self.filter(status='WYKONANA')

    def status_in_progress(self):
        return self.filter(status='W TRAKCIE')


class StatusTodoManager(models.Manager):
    def get_queryset(self):
        return StatusTodoQuerySet(self.model, using=self._db)

    def status_reported(self):
        return self.get_queryset().status_reported()

    def status_contact(self):
        return self.get_queryset().status_contact()

    def status_arranged(self):
        return self.get_queryset().status_arranged()

    def status_done(self):
        return self.get_queryset().status_done()

    def status_in_progress(self):
        return self.get_queryset().status_in_progress()


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=150, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=utils.STATUS_TODO, max_length=30, default='ZGŁOSZONA')
    title = models.CharField(max_length=80, default=None)
    desc = models.TextField(default=None)
    contact_date = models.DateField(null=True)
    date = models.DateField(null=True)
    finish_date = models.DateField(null=True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    objects = StatusTodoManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Todo, self).save(*args, **kwargs)


class ToDoHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    status = models.CharField(choices=utils.STATUS_TODO, max_length=30, default='ZGŁOSZONA')
    old_status = models.CharField(choices=utils.STATUS_TODO, max_length=30, default='ZGŁOSZONA')
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(ToDoHistory, self).save(*args, **kwargs)
