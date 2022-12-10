from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView
from rest_framework import generics, request, response, status
from apps.django_common import views

from . import serializers
from apps.users.models import User


class TokenObtainPairView(views.PublicJSONResponseView, BaseTokenObtainPairView):
    serializer_class = serializers.TokenObtainPairSerializer


class TokenRefreshView(views.PublicJSONResponseView, BaseTokenRefreshView):
    ...


class RegisterView(views.PublicJSONResponseView, generics.GenericAPIView):
    serializer_class = serializers.AuthSerializer

    def post(self, request: request.Request) -> response.Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(**serializer.data)
        jwt_token = serializers.TokenObtainPairSerializer.get_token(user)
        return response.Response(
            data={
                'access': str(jwt_token.access_token),
                'refresh': str(jwt_token),
            }, status=status.HTTP_201_CREATED
        )
