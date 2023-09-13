from django.db import models
from apps.lessons.constans import TIMESLOTS_LESSON  # DAYS_OF_WEEK


class Lesson(models.Model):
    # day_of_week = models.CharField(max_length=20, choices=DAYS_OF_WEEK, verbose_name='День недели')
    name = models.CharField(max_length=100, verbose_name='Имя предмета')
    lesson_time = models.CharField(max_length=100, choices=TIMESLOTS_LESSON, verbose_name='Время уроков')

    def __str__(self):
        return f'{self.name}, {self.date}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Schedule(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Расписание')
    homework = models.TextField(max_length=200, verbose_name='Домашнее задание')
    photo = models.ImageField(verbose_name='Фотография')
    link = models.URLField(verbose_name='Полезные ссылки')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return str(self.lesson)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
