from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from core import models


class MonterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Monter
        fields = ['name', 'type','id']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        exclude = ['created',]


class DailyMontageSerializer(serializers.ModelSerializer):
    daily_montage = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = models.DailyMontage
        fields = ['user', 'team', 'type', 'day_montage', 'date', 'daily_montage']
        validators = [
            UniqueTogetherValidator(
                queryset=models.DailyMontage.objects.all(),
                fields=['team', 'date']
            )
        ]


class MonterDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MonterDaily
        exclude = ['created', 'updated', 'id']
        depth = 1
        validators = [
            UniqueTogetherValidator(
                queryset=models.MonterDaily.objects.all(),
                fields=['name', 'date']
            )
        ]


class DailyMontageCreateSerializer(serializers.ModelSerializer):
    class MonterDailyTempSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.MonterDaily
            exclude = ['daily_montage', 'created', 'updated']
            validators = [
                UniqueTogetherValidator(
                    queryset=models.MonterDaily.objects.all(),
                    fields=['name', 'date']
                )
            ]

    daily_montage = MonterDailyTempSerializer(many=True)

    class Meta:
        model = models.DailyMontage
        exclude = ['created', 'updated']
        validators = [
            UniqueTogetherValidator(
                queryset=models.DailyMontage.objects.all(),
                fields=['team', 'date']
            )
        ]

    def create(self, validated_data):
        model_b_data = validated_data.pop('daily_montage')
        model_a_instance = models.DailyMontage.objects.create(**validated_data)
        for model_b in model_b_data:
            models.MonterDaily.objects.create(daily_montage=model_a_instance,
                                              **model_b)
        return model_a_instance
