from apps.users.constants import CLASS_CHOICES, ROLE_CHOICES
from apps.users.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.Serializer):
    surname = serializers.CharField(min_length=6, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    training_class = serializers.ChoiceField(choices=CLASS_CHOICES)
    role = serializers.ChoiceField(choices=ROLE_CHOICES)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["token"]


class ConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'profile_photo', 'surname', 'email', 'school', 'training_class']
        read_only_fields = ['email', 'training_class']
