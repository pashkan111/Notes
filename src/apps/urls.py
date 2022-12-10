from django.urls import path, include


urlpatterns = [
    path('users/', include('apps.users.api.urls')),
    path('notes/', include('apps.notes_app.api.urls')),
    path('us/', include('apps.users.urls')),
]
