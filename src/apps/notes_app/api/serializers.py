from apps.notes_app import models
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name', )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        exclude = ('author',)
