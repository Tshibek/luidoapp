from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator
from rest_framework import filters
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from core import models
from . import serializers


class MonterApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        monter = models.Monter.objects.all()
        serializer = serializers.MonterSerializer(monter, many=True)
        return Response(serializer.data)


class MonterDailyTodayApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        monter_daily = models.MonterDaily.objects.filter(date=timezone.localdate())
        serializer = serializers.MonterDailyTodaySerializer(monter_daily, many=True)
        return Response(serializer.data)


class MontagePaidApiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        montage_paid = models.MontagePaid.objects.filter(date=timezone.localdate())
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = serializers.DailyMontageCreateSerializer


class MontagePaidCreateApiView(generics.CreateAPIView):
    queryset = models.MontagePaid.objects.all()
    serializers_class = serializers.MontagePaidCreateSerializer
