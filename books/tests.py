from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Book, Tag


class BookModelTests(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(
            title="Total Immersion",
            about="Swimming and stuff",
            current_loc=0,
            isbn='978-0-7432-5434-7'
        )
        now = timezone.now()
        self.assertLess(book.created_at, now)

    def test_book_update(self):
        book = Book.objects.create(
            title="Total Focus",
            about="Focus and things...",
            current_loc=0,
            isbn='978-0-7352-1451-4'
        )
        now = timezone.now()
        self.assertLess(book.created_at, now)
        book.author = 'Brandon Webb'
        book.save()
        self.assertEqual(book.author, 'Brandon Webb')

    def test_book_deletion(self):
        book = Book.objects.create(
            title="It's Only Ray Parlour's Autobiography",
            about="Autobiography of Ray Parlour",
            current_loc=0,
            isbn='978-1-78-475345-0'
        )
        now = timezone.now()
        self.assertLess(book.created_at, now)
        book.delete()
        self.assertEqual(len(Book.objects.all()), 0)


class TabModelTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Total Immersion",
            about="Swimming and stuff",
            current_loc=0,
            isbn='978-0-7432-5434-7'
        )

    def test_tag_creation(self):
        tag = Tag.objects.create(
            name="instruction"
        )
        tag.books.add(self.book)
        self.assertIn(self.book, tag.books.all())

    def test_tag_removal(self):
        tag = Tag.objects.create(
            name="instruction"
        )
        tag.books.add(self.book)
        self.assertIn(self.book, tag.books.all())
        tag.books.remove(self.book)
        self.assertNotIn(self.book, tag.books.all())


class BookViewTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Total Immersion",
            about="Swimming and stuff",
            current_loc=0,
            isbn='978-0-7432-5434-7'
        )

        self.tag = Tag.objects.create(
            name="instruction"
        )
        self.tag.books.add(self.book)

    def test_book_index_view(self):
        resp = self.client.get(reverse('books:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.book, resp.context['books'])
        self.assertTemplateUsed(resp, 'books/index.html')


    def test_book_show_view(self):
        resp = self.client.get(reverse('books:show', args=[self.book.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.book, resp.context['book'])
        self.assertTemplateUsed(resp, 'books/show.html')
        self.assertContains(resp, self.book.title)
