import pytest

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


def test_get_author(book_sample):
    author = data_processing.get_author(book_sample)
    assert author == book_sample['authors'][0]


def test_get_author_when_none(book_sample):
    del book_sample['authors']
    author = data_processing.get_author(book_sample)
    assert author is None


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
