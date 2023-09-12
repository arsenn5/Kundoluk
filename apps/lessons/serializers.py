from rest_framework import serializers

from apps.lessons.models import Lesson, Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['title', 'schedule_time']


class LessonSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'schedule']


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
