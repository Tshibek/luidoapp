from rest_framework import serializers

from core import models


class MonterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Monter
        fields = ['name', 'type']


class DailyMontageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyMontage
        fields = ['type', 'day_montage', 'date', 'user', 'team']
