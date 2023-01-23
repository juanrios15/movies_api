from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    def validate_password(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Length must be at least 10 characters")
        any_lower = any(letter.islower() for letter in value)
        any_upper = any(letter.isupper() for letter in value)
        any_special = any(letter in ["!", "@", "#", "?", "]"] for letter in value)
        if not any_lower or not any_upper or not any_special:
            raise serializers.ValidationError(
                "Password must have at least 1 lowercase letter, 1 uppercase letter and 1 of the following characters: !, @, #, ? or ]."
            )
        return value

    def create(self, validated_data):
        user = User(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get("request"), email=email, password=password)

            if not user:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
