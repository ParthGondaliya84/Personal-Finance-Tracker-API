from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user.views import AuthAPIView, UserProfileAPIView

router = DefaultRouter()
router.register(r'auth', AuthAPIView, basename='auth')
router.register(r'profile', UserProfileAPIView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
