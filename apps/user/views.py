from apps.base.views import BaseViewSet
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.user.models import UserProfile
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from apps.user.serializers import (
    RegisterSerializer,
    LoginSerializer,
    LogoutSerializer,
    UserProfileSerializer
)


class AuthAPIView(viewsets.GenericViewSet):
    serializer_class = RegisterSerializer

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer

        if self.action == 'logout':
            return LogoutSerializer

        return RegisterSerializer

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Account": "Account hase been create Sucessfully"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = authenticate(email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                user_info = {
                    "user_id": user.id,
                    "email": user.email
                }
                return Response(
                    {
                        "Login": "Sucessfully",
                        "user": user_info,
                        "refresh_token": str(refresh),
                        "access_token": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {"Login": "Failed"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    @action(
            detail=False, methods=['post'],
            permission_classes=[IsAuthenticated]
    )
    def logout(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(
                {"error": "refresh_token is required!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"Logout": "sucessfully"},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"error": "Invalid token"},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileAPIView(BaseViewSet, viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get', 'put', 'patch']

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user)
        return queryset
