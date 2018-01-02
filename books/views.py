from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(req):
    books = Book.objects.all()
    return render(req, 'books/index.html', {'books': books})
