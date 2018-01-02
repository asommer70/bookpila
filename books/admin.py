from django.contrib import admin
from .models import Book, Tag

class TagBook(admin.StackedInline):
    model = Tag.books.through

class BookAdmin(admin.ModelAdmin):
    inlines = [TagBook,]

admin.site.register(Book, BookAdmin)
admin.site.register(Tag)
