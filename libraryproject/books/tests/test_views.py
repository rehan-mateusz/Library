import pytest

from django.urls import reverse
from django.test import TestCase

from books import views
from books import models


@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book_data = {
            'title': 'test_title',
            'published_date': '2010-01-01',
            'isbn_13': '1234567890123',
            'pages': '300',
            'cover_link': 'https://samplelink.com',
            'publication_language': 'pl',
            'author_set-TOTAL_FORMS' : '0',
            'author_set-INITIAL_FORMS' : '0',
            'author_set-MIN_NUM_FORMS': '0',
            'author_set-MAX_NUM_FORMS': '5',}

        cls.invalid_form = {
            'intitle': '',
            'inauthor': '',
            'inpublisher': '',
            'subject': '',
            'isbn': '',
            'lcnn': '',
            'oclc': ''}

    def test_BookListView_get(self):
        response = self.client.get(reverse('books:books_list'))
        self.assertEqual(response.status_code, 200)

    def test_BookUpdateOrCreateView_get(self):
        response = self.client.get(reverse('books:book_add'))
        self.assertEqual(response.status_code, 200)

    def test_BookUpdateOrCreateView_post_update_book(self):
        new_book_data = self.book_data
        new_book = models.Book(
            title = new_book_data['title'],
            published_date = new_book_data['published_date'],
            isbn_13 = new_book_data['isbn_13'],
            pages = new_book_data['pages'],
            cover_link = new_book_data['cover_link'],
            publication_language = new_book_data['publication_language'])
        new_book.save()
        new_book_data['title'] = 'new_title'
        response = self.client.post(
            reverse('books:book_update', kwargs={'pk' : new_book.id}),
            new_book_data)
        self.assertTrue(models.Book.objects.get(title='new_title'))
        self.assertEqual(response.status_code, 302)

    def test_BookUpdateOrCreateView_post_add_book(self):
        response = self.client.post(reverse('books:book_add'), self.book_data)
        self.assertTrue(models.Book.objects.get(title='test_title'))
        self.assertEqual(response.status_code, 302)

    def test_GoogleBooksView_get(self):
        response = self.client.get(reverse('books:google_search'))
        self.assertEqual(response.status_code, 200)

    def test_GoogleBooksView_post_with_invalid_data(self):
        response = self.client.post(reverse('books:google_search'),
                                    self.invalid_form)
        self.assertEqual(response.status_code, 200)

    def test_GoogleBooksView_post_with_invalid_data(self):
        valid_form = self.invalid_form
        valid_form['inauthor'] = 'sapkowski'
        response = self.client.post(reverse('books:google_search'), valid_form)
        self.assertEqual(response.status_code, 302)
