from apps.users.models import User
from apps.users.api.serializers import AuthSerializer, UserSerializer
from rest_framework import generics, request, response
from rest_framework.authentication import authenticate
from apps.django_common import views

class LoginView(views.PublicJSONResponseView, generics.GenericAPIView):
    serializer_class = AuthSerializer

    def post(self, request: request.Request) -> response.Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.data)
        if user is None:
            return response.Response(status=401)
        return response.Response(status=200)


class RegisterView(views.PublicJSONResponseView, generics.GenericAPIView):
    serializer_class = AuthSerializer

    def post(self, request: request.Request) -> response.Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(**serializer.data)
        return response.Response(
            UserSerializer(instance=user).data, status=200
        )