from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('api/', include('apps.api_urls')),
]

urlpatterns += swagger_urlpatterns