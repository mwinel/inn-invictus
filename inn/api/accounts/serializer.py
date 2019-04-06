from django.contrib.auth.models import User
from rest_framework import serializers
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
    email = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "token", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    @classmethod
    def validate(cls, data):
        user_obj = None
        username = data.get("username", None)
        password = data.get("password", None)

        if not username:
            raise serializers.ValidationError("Username or email is required to login")

        user = User.objects.filter(Q(email=username) | Q(username=username)).distinct()
        if user.exists():
            user_obj = user.first()
        else:
            raise serializers.ValidationError("Invalid Username/Email")

        if user_obj:
            if not user_obj.password == password:
                raise serializers.ValidationError(
                    "Incorrect credentials please try again "
                )

        data["token"] = "mytoken"
        data["email"] = user_obj.email

        return data
