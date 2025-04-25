from rest_framework import serializers
from apps.base.serializers import BaseSerializer
from apps.transaction.models import Transaction
from apps.category.models import Category


class TransactionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["title", "entry_type"]


class TransactionSerializer(BaseSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )
    category_detail = TransactionCategorySerializer(
        source="category",
        required=False,
        read_only=True
    )
    transaction_date = serializers.DateTimeField(
        read_only=True,
        source="created_at"
    )
    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id", "amount", "category", "category_detail", "note",
            "transaction_type", "created_by", "transaction_date",
        ]

    def validate(self, data):
        amount = data.get('amount')
        zero = 0

        if amount < zero:
            raise serializers.ValidationError({
                "amount": "Amount can not in negative or zero value."
            })

        return data

    def validate_category(self, value):
        if Transaction.objects.filter(category=value).exists():
            raise serializers.ValidationError(
                "A transaction with this category already exists."
            )
        return value
