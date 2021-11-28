import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from core import models
from api import serializers


class MonterApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        monter = models.Monter.objects.all()
        serializer = serializers.MonterSerializer(monter, many=True)
        return Response(serializer.data)


class MonterDailyTodayApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        monter_daily = models.MonterDaily.objects.filter(
            created__gte=timezone.now().replace(hour=0, minute=0, second=0),
            created__lte=timezone.now().replace(hour=23, minute=59, second=59))
        serializer = serializers.MonterDailyTodaySerializer(monter_daily, many=True)
        return Response(serializer.data)


class MontagePaidApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        montage_paid = models.MontagePaid.objects.filter(
            created__gte=timezone.now().replace(hour=0, minute=0, second=0),
            created__lte=timezone.now().replace(hour=23, minute=59, second=59))
        serializer = serializers.MontagePaidSerializer(montage_paid, many=True)
        return Response(serializer.data)


class DailyMontageToday(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        monter = models.DailyMontage.objects.filter(user=self.request.user, date=timezone.localdate()).first()
        serializer = serializers.DailyMontageToday(monter)
        return Response(serializer.data)


class TeamApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        team = models.Team.objects.all()
        serializer = serializers.TeamSerializer(team, many=True)
        return Response(serializer.data)


class MonterDailyApiList(APIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']
    ordering = ['-date']

    def get(self, format=None):
        monter_daily = models.MonterDaily.objects.all().order_by('-date')

        serializer = serializers.MonterDailySerializer(monter_daily, many=True)
        return Response(serializer.data)


class DailyMontageCreateAPIView(generics.CreateAPIView):
    queryset = models.MonterDaily.objects.all()
    serializer_class = serializers.DailyMontageCreateSerializer


class MontagePaidCreateApiView(generics.CreateAPIView):
    queryset = models.MontagePaid.objects.all()
    serializers_class = serializers.MontagePaidCreateSerializer
