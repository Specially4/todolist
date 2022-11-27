from django.contrib.auth import login, get_user, logout
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.models import User
from core.serializers import (
    UserCreateSerializer,
    RetrieveUserSerializer,
    LoginSerializer, PasswordUpdateSerializer
)


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


# @ensure_csrf_cookie
class RetrieveUserView(RetrieveUpdateDestroyAPIView):
    # model = User
    queryset = User.objects.all()
    serializer_class = RetrieveUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        """
        Переопределил для того чтобы при выходе из профиля, пользователь не удалялся из бд.
        """
        logout(request)
        return Response({})


class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer: LoginSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user=user)
        user_serializer = RetrieveUserSerializer(instance=user)
        return Response(user_serializer.data)


class PasswordUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordUpdateSerializer

    def get_object(self):
        return self.request.user
