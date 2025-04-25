import django_filters
from apps.budget.models import Budget


class BudgetFilter(django_filters.FilterSet):
    budget_created_at = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="date",
        label="Budget create date"
    )

    class Meta:
        model = Budget
        fields = ["start_date", "category", "budget_created_at"]
