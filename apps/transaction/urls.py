from rest_framework.routers import DefaultRouter
from apps.transaction.views import TransactionAPIView

router = DefaultRouter()
router.register(r'transaction', TransactionAPIView, basename='transaction')

urlpatterns = router.urls
