from django.urls import path, include


urlpatterns = [
    path('users/', include('users.api.urls')),
    path('notes/', include('notes.api.urls')),
]
