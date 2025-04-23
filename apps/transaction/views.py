from rest_framework import viewsets, status
from apps.base.views import BaseViewSet
from apps.transaction.models import Transaction
from apps.transaction.serializers import TransactionSerializer


class TransactionAPIView(BaseViewSet, viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(created_by=user)
        return queryset
