from django.db import models

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(max_length=1024, blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    current_loc = models.CharField(max_length=255, blank=True, null=True, default="")
    upload = models.FileField(null=True, blank=True)
    cover = models.CharField(max_length=255, blank=True, null=True, default="")
    cover_image = models.ImageField(blank=True, null=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        ordering = ['-updated_at',]

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name
