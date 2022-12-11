from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(title='API для регистрации людей', default_version='v1'),
    authentication_classes=(JWTAuthentication,),
    permission_classes=(permissions.AllowAny,),
    public=True,
)

urlpatterns = [
    path(
        'docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='swagger-ui',
    ),
]
