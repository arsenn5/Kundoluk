from django.contrib import admin
from apps.lessons.models import Schedule, Lesson

# Register your models here.

admin.site.register(Schedule)
admin.site.register(Lesson)
