from django.shortcuts import get_object_or_404, render
from .models import Book

def index(req):
    books = Book.objects.all()
    return render(req, 'books/index.html', {'books': books})


def show(req, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(req, 'books/show.html', {'book': book})
