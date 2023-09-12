from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView

from apps.lessons.models import Lesson
from apps.lessons.serializers import LessonSerializer, LessonDetailSerializer
from apps.users.permission import IsElderPermission, IsStudentPermission, IsStudentOrElderPermission


# Create your views here.

class LessonAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsStudentOrElderPermission,)


class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = (IsStudentOrElderPermission,)
    lookup_field = 'id'


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = (IsElderPermission,)
