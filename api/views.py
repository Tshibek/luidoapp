from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
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
        serializer = serializers.MonterSerializer(monter, many=True)
        return Response(serializer.data)


class TeamApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        team = models.Team.objects.all()
        serializer = serializers.TeamSerializer(team, many=True)
        return Response(serializer.data)


class MonterDailyApiList(APIView):
    permission_classes = [IsAuthenticated]
    ordering = ['-date']

    def get(self, format=None):
        monter_daily = models.MonterDaily.objects.all()
        serializer = serializers.MonterDailySerializer(monter_daily, many=True)
        return Response(serializer.data)


class DailyMontageCreateAPIView(generics.CreateAPIView):
    queryset = models.MonterDaily.objects.all()
    serializer_class = serializers.DailyMontageCreateSerializer
