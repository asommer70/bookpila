from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
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
            'cover'
        )
        model = models.Book


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
        )
        model = models.Tag
