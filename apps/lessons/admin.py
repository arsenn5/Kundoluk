from django.contrib import admin
from .models import Lesson, Schedule, Date


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'lesson_time']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'homework']


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ['date']
