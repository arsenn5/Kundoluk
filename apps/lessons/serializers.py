from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.lessons.models import Lesson, Schedule, Date


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'lesson_time']


class ScheduleSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Schedule
        fields = ['id', 'lesson', 'date']


class ScheduleDetailSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Schedule
        fields = "__all__"
        # read_only_fields = ['training_class', 'user']


class DateSerializer(serializers.ModelSerializer):
    # lesson = ScheduleSerializer(many=True)
    date = serializers.DateField(validators=[UniqueValidator(queryset=Date.objects.all())])

    class Meta:
        model = Date
        fields = ['id', 'date', 'lesson', 'training_class', 'user']
        read_only_fields = ['training_class', 'user']
