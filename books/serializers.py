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
    tags = TagSerializer(read_only=True, many=True)
    cover_image = serializers.ImageField(read_only=True)
    upload = serializers.FileField(read_only=True)

    class Meta:
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'author',
            'about',
            'isbn',
            'current_loc',
            'upload',
            'cover',
            'cover_image',
            'tags'
        )
        model = models.Book
