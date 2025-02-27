from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from apps.users.emails import send_email_confirm
from apps.users.models import User
from apps.users.serializers import RegisterSerializer, LoginSerializer, ConfirmSerializer, ProfileSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = User.objects.get(email=serializer.validated_data['email'])
        send_email_confirm(user.email)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response(
                {
                    'messege': 'authenticate successfully',
                    "status": status.HTTP_200_OK,
                    "surname": user.surname,
                    'email': user.email,
                    "refresh_token": str(refresh),
                    "access_token": str(access)
                }
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'username or password incorrect!'})

    def list(self, request):
        return Response(status=status.HTTP_200_OK)


class ConfirmAPIView(CreateAPIView):
    serializer_class = ConfirmSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        code = serializer.data['code']

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'Неверный email.'}, status=400)

        if user.code != code:
            return Response({'error': 'Неверный код подтверждения.'}, status=400)

        user.is_active = True
        user.save()

        return Response({'message': 'Аккаунт успешно подтвержден.'}, status=200)


class ProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_class = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)
