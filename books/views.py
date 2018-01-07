from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book, Tag
from .forms import BookForm, TagForm
from .book_manipulations import *

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
            # Pull out the first page of a PDF file and create an image from it.
            if (new_book.upload.name[-3:] == 'pdf'):
                new_book.cover = get_pdf_cover(new_book)
                new_book.save()

            if (new_book.upload.name[-4:] == 'epub'):
                new_book.cover = get_epub_cover(new_book)
                new_book.save()
                
            messages.add_message(req, messages.SUCCESS, "Book {} created...".format(new_book.title))
            return HttpResponseRedirect(reverse('books:show', args=[new_book.pk]))

    return render(req, 'books/new.html', {'form': form})


@login_required
def edit(req, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book)
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES, instance=book)
        if form.is_valid():
            form.save()

            # Pull out the first page of a PDF file and create an image from it.
            if (book.upload.name[-3:] == 'pdf'):
                book.cover = get_pdf_cover(book)
                book.save()

            if (book.upload.name[-4:] == 'epub'):
                book.cover = get_epub_cover(book)
                book.save()

            messages.success(req, "{} has been updated.".format(book.title))
            return HttpResponseRedirect(reverse('books:show', args=[book.pk]))
    return render(req, 'books/edit.html', {'book': book, 'form': form})


@login_required
def delete(req, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(req, "{} has been deleted.".format(book.title))
    return HttpResponseRedirect(reverse('books:index'))


@login_required
def search(req, term):
    books = Book.objects.filter(title__icontains=term)
    return render(req, 'books/index.html', {'books': books, 'term': term})


@login_required
def remove_tag(req, pk):
    if req.method == 'POST':
        book = Book.objects.get(id=pk)
        tag = Tag.objects.get(id=req.POST['tagid'])
        tag.books.remove(book)
        book.save()
        messages.success(req, "{} has been removed.".format(tag.name))
        return JsonResponse({'message': "{} has been removed.".format(tag.name)})
    else:
        return HttpResponseRedirect(reverse('books:show', args=[book.id]))


@login_required
def tag(req, pk):
    tag = Tag.objects.get(id=pk)
    return render(req, 'books/tag.html', {'tag': tag})
