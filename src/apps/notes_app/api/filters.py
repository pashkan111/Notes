from django_filters import rest_framework as filters
from apps.notes_app.models import Note


class NoteFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__name")
    created = filters.CharFilter(field_name="created")
    name = filters.CharFilter(field_name="name")
    is_liked = filters.CharFilter(field_name="is_liked")

    class Meta:
        model = Note
        fields = {}
