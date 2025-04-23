from rest_framework import viewsets
from apps.base.views import BaseViewSet
from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from apps.category.filters import CategoryFilters
from django_filters.rest_framework import DjangoFilterBackend


class CategoryAPIView(BaseViewSet, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilters

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(created_by=user)
        return queryset
