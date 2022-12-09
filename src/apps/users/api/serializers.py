from apps.users.models import User
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    mobile_phone = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=50)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('created_at', 'mobile_phone')