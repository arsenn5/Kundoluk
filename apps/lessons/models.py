from django.db import models

from apps.lessons.constans import TIMESLOTS_SCHEDULE


# Create your models here.
class Schedule(models.Model):
    title = models.CharField(max_length=100, null=True)
    schedule_time = models.CharField(max_length=100, choices=TIMESLOTS_SCHEDULE)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
    homework = models.TextField(max_length=200)
    photo = models.ImageField()
    link = models.URLField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.schedule} - {self.homework}"
