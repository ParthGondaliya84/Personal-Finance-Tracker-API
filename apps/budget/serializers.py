from rest_framework import serializers
from apps.base.serializers import BaseSerializer
from apps.category.models import Category
from apps.budget.models import Budget


class BudgetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "entry_type"]


class BudgetSerializer(BaseSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )
    category_detail = BudgetCategorySerializer(
        read_only=True,
        source="category",
        required=False,
    )

    class Meta:
        model = Budget
        fields = [
            "id", "category", "amount", "start_date", "end_date",
            "category_detail", "created_at",
        ]

    def validate(self, data):
        amount = data.get("amount")
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        zero = 0

        if amount <= zero:
            raise serializers.ValidationError({
                "amount": "Amount can not in negative or zero value"
            })

        if (
            start_date is not None and end_date is not None and
            end_date < start_date
        ):
            raise serializers.ValidationError({
                "end_date": "End date cannot be before start date."
            })

        return data
