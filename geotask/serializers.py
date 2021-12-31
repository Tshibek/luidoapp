from rest_framework import serializers
from . import models


class ClientGeotaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        depth = 1
        fields = ['order_number', 'last_name', ]


class ProjectGeoTaskSerializer(serializers.ModelSerializer):
    client = ClientGeotaskSerializer(read_only=True)

    class Meta:
        model = models.Project
        many = True
        fields = ['file']


class TaskGeotaskSerializer(serializers.ModelSerializer):
    client = ClientGeotaskSerializer(read_only=True)

    class Meta:
        model = models.Task
        many = True
        fields = ['type', 'team', 'date']


class StatusTaskGeoTaskSerializer(serializers.ModelSerializer):
    task = TaskGeotaskSerializer(read_only=True)
    class Meta:
        model = models.StatusTask
        many = True
        fields = ['status']


class TaskGalleryGeotaskSerializer(serializers.ModelSerializer):
    task = TaskGeotaskSerializer(read_only=True)

    class Meta:
        model = models.TaskGallery
        depth = 1
        many = True
        fields = ['images']


class CommentTaskSerializer(serializers.ModelSerializer):
    task = TaskGeotaskSerializer(read_only=True)

    class Meta:
        many = True
        model = models.CommentTask
