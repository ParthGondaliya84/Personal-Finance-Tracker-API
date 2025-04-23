from rest_framework import serializers
from apps.base.serializers import BaseSerializer
from apps.category.models import Category


class CategorySerializer(BaseSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = [
            "id", "created_by", "updated_by", "is_active", "is_delete"
        ]
