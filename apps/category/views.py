from rest_framework import viewsets
from apps.base.views import BaseViewSet
from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class CategoryAPIView(BaseViewSet, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(created_by=user)
        return queryset
