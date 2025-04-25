from rest_framework import viewsets, status
from apps.base.views import BaseViewSet
from apps.transaction.models import Transaction
from apps.transaction.serializers import TransactionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.transaction.filters import TransactionFilter


class TransactionAPIView(BaseViewSet, viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter
    http_method_names = ["get", "post"]

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(created_by=user)
        return queryset
