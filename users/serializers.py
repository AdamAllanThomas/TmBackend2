from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "name",
            "email",
            "password",
            "phone",
            "profile_image",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True,
            }
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        profile_image = validated_data.pop("profile_image", None)
        if profile_image:
            instance.profile_image.save(profile_image.name, profile_image)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
