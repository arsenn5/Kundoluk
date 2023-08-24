from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.users.constants import ROLE_CHOICES, CLASS_CHOICES
from apps.users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    surname = models.CharField(max_length=100, null=True, unique=True, verbose_name='ФИО')
    email = models.EmailField(max_length=100, null=True, unique=True, verbose_name='Почта')
    password = models.CharField(max_length=100, unique=True, verbose_name='Пароль')
    training_class = models.CharField(choices=CLASS_CHOICES, null=True, max_length=100, verbose_name='Класс')
    role = models.CharField(choices=ROLE_CHOICES, null=True, max_length=100, verbose_name='Роль')
    code = models.CharField(max_length=6)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_elder = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'surname']

    objects = UserManager()

    def __str__(self):
        return self.email

    app_label = 'users'
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'