from django.urls import path
from . import views


urlpatterns = [
    path('notes', views.NoteView.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('notes/<uuid:guid>', views.NoteView.as_view({
        "put": "update", "delete": "destroy", "get": "retrieve"
    })),
    path('categories', views.CategoryListView.as_view()),
]
