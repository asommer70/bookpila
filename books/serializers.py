from rest_framework import serializers
from . import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'books'
        )
        model = models.Tag
        


class BookSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=False, many=True)
    # tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'author',
            'about',
            'isbn',
            'file_url',
            'current_loc',
            'upload',
            'cover',
            'tags'
        )
        model = models.Book
