from django.urls import path

from apps.lessons.views import LessonAPIView, LessonCreateAPIView, LessonDetailAPIView

urlpatterns = [
    path('lesson/', LessonAPIView.as_view(), name='list_lesson'),
    path('lesson/<int:id>/', LessonDetailAPIView.as_view(), name='list_lesson'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='list_lesson')
]
