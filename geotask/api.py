from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . import models
from rest_framework.response import Response
from . import serializers


class ClientApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        client = models.Client.objects.all()
        serializer = serializers.ClientGeotaskSerializer(client, many=True)
        return Response(serializer.data)


class TaskApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        task = models.Task.objects.all()
        serializer = serializers.TaskGeotaskSerializer(task, many=True)
        return Response(serializer.data)


class TaskGalleryApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        gallery = models.TaskGallery.objects.all()
        serializer = serializers.TaskGalleryGeotaskSerializer(gallery, many=True)
        return Response(serializer.data)


class CommentTaskApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        comment = models.CommentTask.objects.all()
        serializer = serializers.CommentTaskSerializer(comment, many=True)
        return Response(serializer.data)
