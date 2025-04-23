from apps.base.serializers import BaseSerializer
from apps.transaction.models import Transaction


class TransactionSerializer(BaseSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = [
            "id", "created_by", "updated_by", "created_at", "updated_at",
            "is_active", "is_delete"
        ]
