from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_superuser',)
        read_only_fields = ('is_active', 'is_superuser',)
