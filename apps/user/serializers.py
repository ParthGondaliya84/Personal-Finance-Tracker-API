from rest_framework import serializers
from apps.base.serializers import BaseSerializer
from apps.user.models import PFTUser, UserProfile


class RegisterSerializer(BaseSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = PFTUser
        fields = [
            "email", "password", "re_password", "gender"
        ]
        extra_kwargs = {
            "email": {"validators": []}
        }

    def validate_email(self, data):
        normalized_email = data.lower()
        if PFTUser.objects.filter(
            email__iexact=normalized_email
        ).exists():
            raise serializers.ValidationError(
                'This email is already registered')
        return normalized_email

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data["email"] = validated_data["email"].lower()
        user = PFTUser.objects.create_user(
            email=validated_data["email"].lower(),
            gender=validated_data["gender"],
            password=validated_data["password"]
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = PFTUser
        fields = ["email"]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = [
            "id", "user", "created_by", "created_at", "updated_by",
            "updated_at"
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)

        if user_data:
            user_serialziers = UserSerializer(
                instance.user, data=user_data, partial=True
            )

            if user_serialziers.is_valid():
                user_serialziers.save()
            else:
                raise serializers.ValidationError(user_serialziers.errors)

        return super().update(instance, validated_data)
