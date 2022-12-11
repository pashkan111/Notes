from apps.notes_app import models
from rest_framework import serializers
from apps.django_common.exceptions import NoCategoryError


class SerializerWriteAllowMethodField(serializers.SerializerMethodField):
    def __init__(self, method_name=None, **kwargs):
        super().__init__(method_name, **kwargs)
        self.read_only = False

    def to_internal_value(self, data):
        return {self.field_name: data}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class NoteSerializer(serializers.ModelSerializer):
    category = SerializerWriteAllowMethodField()
    class Meta:
        model = models.Note
        exclude = ('author',)

    def get_category(self, obj):
        return obj.category.name

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category = models.Category.objects.filter(
            name=category_name
        ).first()
        if category is None:
            raise NoCategoryError

        note = models.Note.objects.create(
            **validated_data, category=category
        )
        return note

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category')
        validated_data.setdefault('category_id', category_id)
        return super().update(instance, validated_data)