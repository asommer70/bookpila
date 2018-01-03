from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Book
from .forms import ContactForm

def index(req):
    books = Book.objects.all()
    return render(req, 'books/index.html', {'books': books})


def show(req, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(req, 'books/show.html', {'book': book})


def edit(req, pk):
    contact_form = ContactForm()
    book = get_object_or_404(Book, pk=pk)
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            print('ContactForm is valid...')
            messages.add_message(req, messages.SUCCESS, 'Thanks for the message!')
            return HttpResponseRedirect(reverse('books:show', args=[book.pk]))
    return render(req, 'books/edit.html', {'book': book, 'contact_form': contact_form})
