from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer

from apps.django_common.exceptions import NoActiveAccountError


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    username_field = "mobile_phone"

    def validate(self, attrs):
        try:
            attrs["request"] = self.context["request"]
        except KeyError:
            pass
        self.user = authenticate(**attrs)

        if self.user is None or not self.user.is_active:
            raise NoActiveAccountError
        refresh = self.get_token(self.user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return data

    # @classmethod
    # def get_token(cls, user: "User"):
    #     token = super().get_token(user)
    #     token['mobile_phone'] = user.mobile_phone.as_e164

    #     try:
    #         if user.employee:
    #             token["full_name"] = user.employee.full_name
    #     except ObjectDoesNotExist:
    #         pass

    #     return token


class TokenOutputSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class AuthSerializer(serializers.Serializer):
    mobile_phone = serializers.CharField(max_length=11)
    password = serializers.CharField(max_length=50)
