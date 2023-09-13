from django.contrib import admin
from .models import Lesson, Schedule

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'lesson_time']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'homework', 'date']
