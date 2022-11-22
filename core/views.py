from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.models import User
from core.serializers import UserCreateSerializer, RetrieveUserSerializer


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


@ensure_csrf_cookie
class RetrieveUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RetrieveUserSerializer
    permission_classes = [IsAuthenticated]
