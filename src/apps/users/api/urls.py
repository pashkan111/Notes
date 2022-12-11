from django.urls import path

from .views import TokenObtainPairView, RegisterView, TokenRefreshView

urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("register", RegisterView.as_view(), name="register"),
]
