from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


@login_required
def index(req):
    books = Book.objects.all()
    return render(req, 'books/index.html', {'books': books})


@login_required
def show(req, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(req, 'books/show.html', {'book': book})


@login_required
def new(req):
    # book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            new_book = form.save()
            messages.add_message(req, messages.SUCCESS, "Book {} created...".format(new_book.title))
            return HttpResponseRedirect(reverse('books:show', args=[new_book.pk]))

    return render(req, 'books/new.html', {'form': form})


@login_required
def edit(req, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book)
    if req.method == 'POST':
        form = BookForm(instance=book, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "{} has been updated.".format(book.title))
            return HttpResponseRedirect(reverse('books:show', args=[book.pk]))
    return render(req, 'books/edit.html', {'book': book, 'form': form})
