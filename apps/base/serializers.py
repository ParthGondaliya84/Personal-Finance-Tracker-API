from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        abstract = True
        read_only_fields = [
            "created_by", "created_at", "updated_by", "updated_at",
            "is_active", "is_delete"
        ]
