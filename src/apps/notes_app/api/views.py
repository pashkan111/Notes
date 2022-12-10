from . import serializers
from rest_framework import generics, viewsets
from apps.django_common import views
from apps.notes_app import models
from .filters import NoteFilter


class CategoryListView(views.PublicJSONResponseView, generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class NoteView(views.JSONResponseView, viewsets.ModelViewSet):
    serializer_class = serializers.NoteSerializer
    lookup_field = 'guid'
    filterset_class = NoteFilter
    
    def get_queryset(self):
        notes = models.Note.objects.select_related('category')\
            .filter(author=self.request.user)
        return notes

    def perform_create(self, serializer: serializers.NoteSerializer):
        serializer.save(author=self.request.user)

