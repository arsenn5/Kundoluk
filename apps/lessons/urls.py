from django.urls import path

from apps.lessons.views import ScheduleAPIView, ScheduleCreateAPIView, ScheduleDetailAPIView

urlpatterns = [
    path('lesson/', ScheduleAPIView.as_view(), name='list_lesson'),
    path('lesson/<int:id>/', ScheduleDetailAPIView.as_view(), name='list_lesson'),
    path('lesson/create/', ScheduleCreateAPIView.as_view(), name='list_lesson')
]
