from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView

from apps.lessons.models import Schedule, Date
from apps.lessons.serializers import ScheduleSerializer, ScheduleDetailSerializer, DateSerializer
from apps.users.permission import IsElderPermission, IsStudentPermission, IsStudentOrElderPermission
from apps.lessons.filters import ScheduleFilter


class ScheduleDetailAPIView(RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer
    permission_classes = (IsStudentOrElderPermission,)
    lookup_field = 'id'


class ScheduleCreateAPIView(CreateAPIView):
    serializer_class = ScheduleDetailSerializer
    permission_classes = (IsElderPermission,)

    def perform_create(self, serializer):
        user_class = self.request.user.training_class
        user = self.request.user

        serializer.save(training_class=user_class, user=user)


class ScheduleAPIView(ListAPIView):
    serializer_class = DateSerializer
    permission_classes = [IsStudentOrElderPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter

    def get_queryset(self):
        user = self.request.user

        user_class = user.training_class

        queryset = Date.objects.filter(training_class=user_class)

        return queryset


class ScheduleListAPIView(CreateAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
    permission_classes = [IsElderPermission]

    def perform_create(self, serializer):
        user_class = self.request.user.training_class
        user = self.request.user

        serializer.save(training_class=user_class, user=user)

