from django.urls import path

from apps.users.views import RegisterAPIView, LoginAPIView, ConfirmAPIView, ProfileAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('confirm/', ConfirmAPIView.as_view(), name='confirm'),
    path('profile/', ProfileAPIView.as_view(), name='profile_user')
]
