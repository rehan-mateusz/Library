import pytest

from books import models
from books import data_processing


@pytest.mark.parametrize(
    'key',
    [('title'), ('pagesCount'), ('language'), ],
)
def test_get_value(book_sample, key):
    value = data_processing.get_value(book_sample, key)
    assert value == book_sample[key]


@pytest.mark.parametrize(
    'key',
    [('title'), ('pagesCount'), ('language'), ],
)
def test_get_value_when_none(book_sample, key):
    del book_sample[key]
    value = data_processing.get_value(book_sample, key)
    assert value is None


def test_get_authors(book_sample):
    authors = data_processing.get_authors(book_sample)
    assert authors == book_sample['authors']


def test_get_authors_when_none(book_sample):
    del book_sample['authors']
    authors = data_processing.get_authors(book_sample)
    assert authors is None


@pytest.mark.parametrize(
    'test_date',
    [
        ('2010-01-01'), ('2010-01-1'), ('2010-1-01'),
        ('2010-01'), ('2010-1'), ('2020')
    ],
)
def test_get_pub_date(book_sample, test_date):
    book_sample['publishedDate'] = test_date
    fixed_date = data_processing.get_pub_date(book_sample)
    assert fixed_date.count('-') == 2 and len(fixed_date) <= 10


def test_get_pub_date_when_none(book_sample):
    del book_sample['publishedDate']
    fixed_date = data_processing.get_pub_date(book_sample)
    assert fixed_date is None


def test_get_isbn(book_sample):
    isbn = data_processing.get_isbn(book_sample)
    assert isbn == book_sample['industryIdentifiers'][0]['identifier']


def test_get_isbn_with_no_indentifiers(book_sample):
    del book_sample['industryIdentifiers']
    isbn = data_processing.get_isbn(book_sample)
    assert isbn is None


def test_get_isbn_with_only_non_13_identifiers(book_sample):
    book_sample['industryIdentifiers'][0]['type'] = 'OTHER'
    isbn = data_processing.get_isbn(book_sample)
    assert isbn is None


def test_get_image_url_with_two_links_avaliable(book_sample):
    cover_link = data_processing.get_image_url(book_sample)
    assert cover_link == book_sample['imageLinks']['thumbnail']


def test_get_image_url_with_only_small_thumbnail_avaliable(book_sample):
    del book_sample['imageLinks']['thumbnail']
    cover_link = data_processing.get_image_url(book_sample)
    assert cover_link == book_sample['imageLinks']['smallThumbnail']


def test_get_image_url_with_none(book_sample):
    del book_sample['imageLinks']
    cover_link = data_processing.get_image_url(book_sample)
    assert cover_link is None


def test_get_books_model_data(book, book_model_data_list):
    books_list = [book]
    test_books_model_data_list = data_processing.get_books_model_data(
        books_list)
    assert test_books_model_data_list == book_model_data_list

@pytest.mark.django_db
def test_save_new_book_or_get_original_creates_book(book_model_data_list):
    book_model = book_model_data_list[0]['book_model_data']
    new_book = data_processing.save_new_book_or_get_original(book_model)
    assert models.Book.objects.get(**book_model)

@pytest.mark.django_db
def test_save_new_book_or_get_original_returns_original(book_model_data_list):
    book_model = book_model_data_list[0]['book_model_data']
    old_book = models.Book(**book_model)
    old_book.save()
    new_book = data_processing.save_new_book_or_get_original(book_model)
    assert old_book == new_book

@pytest.mark.django_db
def test_save_books_creates_book(book_model_data_list):
    book_model = book_model_data_list[0]['book_model_data']
    data_processing.save_books(book_model_data_list)
    assert models.Book.objects.get(**book_model)

@pytest.mark.django_db
def test_save_form_and_formset_creates_book(book_form, author_formset):
    data_processing.save_form_and_formset(book_form, author_formset)
    assert models.Book.objects.get(**book_form.cleaned_data)
