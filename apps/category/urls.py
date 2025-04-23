from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.category.views import CategoryAPIView

router = DefaultRouter()
router.register(r'category', CategoryAPIView, basename='category')

# urlpatterns = [
#     path('', include(router.urls)),

# ]
urlpatterns = router.urls
