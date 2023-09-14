from django.urls import path

from apps.lessons.views import ScheduleAPIView, ScheduleCreateAPIView, ScheduleDetailAPIView, ScheduleListAPIView

urlpatterns = [
    path('lesson/', ScheduleAPIView.as_view(), name='list_lesson'),
    path('lesson/schedule/', ScheduleListAPIView.as_view(), name='list_lesson'),
    path('lesson/<int:id>/', ScheduleDetailAPIView.as_view(), name='list_lesson'),
    path('lesson/create/', ScheduleCreateAPIView.as_view(), name='list_lesson')
]
