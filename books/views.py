from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book, Tag
from .forms import BookForm, TagForm


@login_required
def index(req):
    books = Book.objects.all()
    return render(req, 'books/index.html', {'books': books})


@login_required
def show(req, pk):
    book = get_object_or_404(Book, pk=pk)
    tag_form = TagForm()

    if req.method == 'POST':
        tag_form = TagForm(req.POST)
        if tag_form.is_valid():
            for string in tag_form.cleaned_data['tags'].split(','):
                tag = Tag.objects.get_or_create(name=string.strip())
                tag[0].books.add(book)
                tag[0].save()

            messages.add_message(req, messages.SUCCESS, "Tags added...")
            return HttpResponseRedirect(reverse('books:show', args=[book.pk]))
        else:
            messages.add_message(req, messages.ALERT, "Problem adding tags...")
            return HttpResponseRedirect(reverse('books:show', args=[book.pk]))
    return render(req, 'books/show.html', {'book': book, 'tag_form': tag_form})


@login_required
def new(req):
    form = BookForm()
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES)
        if form.is_valid():
            new_book = form.save()
            messages.add_message(req, messages.SUCCESS, "Book {} created...".format(new_book.title))
            return HttpResponseRedirect(reverse('books:show', args=[new_book.pk]))

    return render(req, 'books/new.html', {'form': form})


@login_required
def edit(req, pk):
    book = get_object_or_404(Book, pk=pk)
    # form = BookForm(instance=book)
    form = BookForm(instance=book)
    if req.method == 'POST':
        # form = BookForm(instance=book, data=req.POST, upload=req.FILES)
        print('req.FILES:', req.FILES)
        print('req.POST:', req.POST)
        form = BookForm(req.POST, req.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(req, "{} has been updated.".format(book.title))
            return HttpResponseRedirect(reverse('books:show', args=[book.pk]))
    return render(req, 'books/edit.html', {'book': book, 'form': form})


@login_required
def delete(req, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(req, "{} has been deleted.".format(book.title))
    return HttpResponseRedirect(reverse('books:index'))
