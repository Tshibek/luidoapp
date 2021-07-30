from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from . import utils


class Monter(models.Model):
    name = models.CharField(max_length=15)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Monter, self).save(*args, **kwargs)


class Team(models.Model):
    team = models.CharField(max_length=15, unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.team


class DailyMontage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=utils.TYPE, max_length=35, default='Montaż')
    day_montage = models.CharField(choices=utils.DAY_MONTAGE, max_length=8, default='1/1')
    date = models.DateField(null=True,blank=True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def __str__(self):
        return '{}-{}/{}'.format(self.team.team, self.type, self.date)

    def monter_daily(self):
        monter_daily = MonterDaily.objects.filter(daily_montage=self.pk).first()
        return monter_daily

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(DailyMontage, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['team', 'date'], name='name of daily montage')
        ]


class MonterDaily(models.Model):
    name = models.ForeignKey(Monter, on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=utils.STATUS, max_length=30, default='PRACUJE')
    daily_montage = models.ForeignKey(DailyMontage, on_delete=models.SET_NULL, null=True)
    time_start = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    daily_hours = models.TimeField(blank=True, null=True)
    date = models.DateField(null=True,blank=True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def __str__(self):
        return '{},{}'.format(self.name, self.status)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(MonterDaily, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'date'], name='name of monter work')
        ]


class MontagePaid(models.Model):
    montage = models.ForeignKey(DailyMontage, on_delete=models.CASCADE)
    days = models.CharField(choices=utils.DAYS, default='Jednodniówka', max_length=30)
    date = models.DateField(null=True,blank=True)
    paid = models.PositiveSmallIntegerField(default=0)
    cabinet = models.PositiveSmallIntegerField(default=0)  # ilość szafek
    comment = models.TextField(blank=True, null=True)
    build = models.BooleanField(default=False)
    cornice = models.BooleanField(default=False)
    turnbuckles = models.SmallIntegerField(default=1)  # śruby rzymskie
    type_table = models.CharField(max_length=40)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def __str__(self):
        return '{},{}'.format(self.days, self.date)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(MontagePaid, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['montage', 'date'], name='name of montage paid')
        ]
