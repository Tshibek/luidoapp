from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core import models
from api import serializers


class MonterApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        monter = models.Monter.objects.all()
        serializer = serializers.MonterSerializer(monter,many=True)
        return Response(serializer.data)


class DailyMontageApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        daily_montage = models.DailyMontage.objects.all()
        serializer = serializers.DailyMontageSerializer(daily_montage, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.DailyMontageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
