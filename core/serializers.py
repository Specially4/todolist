from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from core.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[
         UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(min_length=1)
    password_repeat = serializers.CharField(min_length=1)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password_repeat'
        ]

    def validate(self, attrs):
        password_repeat = attrs.pop('password_repeat')
        password = attrs.get('password')

        if password_repeat != password:
            raise ValidationError('Passwords do not match')
        return attrs


class RetrieveUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]
