from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from core import models


class MonterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Monter
        fields = ['name', 'type']


class DailyMontageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=models.Team.objects.all())

    class Meta:
        model = models.DailyMontage
        fields = ['user', 'team', 'type', 'day_montage', 'date']
        validators = [
            UniqueTogetherValidator(
                queryset=models.DailyMontage.objects.all(),
                fields=['team', 'date']
            )
        ]


class MonterDailySerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(queryset=models.Monter.objects.all())
    daily_montage = serializers.PrimaryKeyRelatedField(queryset=models.DailyMontage.objects.all())
    class Meta:
        model = models.MonterDaily
        fields = ['name', 'daily_montage', 'status', 'time_start','date']
        validators = [
            UniqueTogetherValidator(
                queryset=models.MonterDaily.objects.all(),
                fields=['name', 'date']
            )
        ]