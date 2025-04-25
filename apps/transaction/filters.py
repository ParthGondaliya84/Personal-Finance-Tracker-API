import django_filters
from apps.transaction.models import Transaction
from apps.category.constant import CategoryType


class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.MultipleChoiceFilter(
        choices=CategoryType.choice(),
        method="transaction_type_filter"
    )

    def transaction_type_filter(self, queryset, name, value):
        return queryset.filter(transaction_type__in=value)

    transaction_date = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="date",
    )

    class Meta:
        model = Transaction
        fields = ["category", "transaction_type",]
