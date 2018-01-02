from django.db import models

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    about = models.TextField(max_length=1024)
    isbn = models.CharField(max_length=100)
    file_url = models.URLField(blank=True, default="")
    current_loc = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name
