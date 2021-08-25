from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from core import models


class MonterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Monter
        fields = ['name', 'type']


class DailyMontageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyMontage
        fields = ['type', 'day_montage', 'date', 'user', 'team']
        validators = [
            UniqueTogetherValidator(
                queryset=models.DailyMontage.objects.all(),
                fields=['team', 'date']
            )
        ]
