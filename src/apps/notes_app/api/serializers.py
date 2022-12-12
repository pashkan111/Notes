from apps.notes_app import models
from rest_framework import serializers
from apps.django_common.exceptions import NoCategoryError



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')

class CategoryNoteSerializer(serializers.CharField):
    def to_internal_value(self, data):
        cat = models.Category.objects.get(id=data)
        return cat

class NoteSerializer(serializers.ModelSerializer):
    category = CategoryNoteSerializer()
    class Meta:
        model = models.Note
        exclude = ('author',)
