from rest_framework import viewsets
from apps.base.views import BaseViewSet
from apps.budget.models import Budget
from apps.budget.serializers import BudgetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.budget.filters import BudgetFilter


class BudgetAPIView(BaseViewSet, viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BudgetFilter

    def get_queryset(self):
        user = self.request.user
        queryset = Budget.objects.filter(created_by=user)
        return queryset
