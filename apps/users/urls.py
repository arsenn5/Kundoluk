from django.urls import path

from apps.users.views import RegisterAPIView, LoginAPIView, ConfirmAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('confirm/', ConfirmAPIView.as_view(), name='confirm')
]
