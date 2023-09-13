from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView

from apps.lessons.models import Schedule
from apps.lessons.serializers import ScheduleSerializer, ScheduleDetailSerializer
from apps.users.permission import IsElderPermission, IsStudentPermission, IsStudentOrElderPermission
from apps.lessons.filters import ScheduleFilter


class ScheduleAPIView(ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsStudentOrElderPermission,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter


class ScheduleDetailAPIView(RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer
    permission_classes = (IsStudentOrElderPermission,)
    lookup_field = 'id'


class ScheduleCreateAPIView(CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer
    permission_classes = (IsElderPermission,)
