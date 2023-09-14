from django.db import models
from apps.lessons.constans import TIMESLOTS_LESSON  # DAYS_OF_WEEK
from apps.users.constants import CLASS_CHOICES
from apps.users.models import User


class Lesson(models.Model):
    # day_of_week = models.CharField(max_length=20, choices=DAYS_OF_WEEK, verbose_name='День недели')
    name = models.CharField(max_length=100, verbose_name='Имя предмета')
    lesson_time = models.CharField(max_length=100, choices=TIMESLOTS_LESSON, verbose_name='Время уроков')

    def __str__(self):
        return f'предмет: {self.name} время урока: {self.lesson_time} ---'

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
        return f'{str(self.lesson)} Дата : {self.date}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Date(models.Model):
    date = models.DateField(verbose_name='Дата')
    lesson = models.ManyToManyField(Schedule, verbose_name='Урок', related_name='dates')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    training_class = models.CharField(choices=CLASS_CHOICES, null=True, max_length=100, verbose_name='Класс')

    # training_class = models.CharField(choices=CLASS_CHOICES, null=True, max_length=100, verbose_name='Класс')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'
