from rest_framework.routers import DefaultRouter
from apps.budget.views import BudgetAPIView

router = DefaultRouter()
router.register(r'budget', BudgetAPIView, basename="budget")

urlpatterns = router.urls
