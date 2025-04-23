import django_filters
from apps.category.models import Category
from apps.category.constant import CategoryType


class CategoryFilters(django_filters.FilterSet):
    entry_type = django_filters.MultipleChoiceFilter(
        choices=CategoryType.choice(),
        method="entry_type_filter"
    )

    def entry_type_filter(self, queryset, name, value):
        return queryset.filter(entry_type__in=value)

    class Meta:
        model = Category
        fields = ["title", "entry_type",]
