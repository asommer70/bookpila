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
    cover_url = serializers.SerializerMethodField()

    def get_cover_url(self, obj):
        request = self.context.get('request')

        if obj.cover_image:
            return request.build_absolute_uri(obj.cover_image.url)
        elif obj.cover:
            return request.build_absolute_uri(obj.cover)


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
            'cover_url',
            'tags'
        )
        # exclude = ['cover']
        model = models.Book
