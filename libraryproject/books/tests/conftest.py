import pytest

@pytest.fixture
def book_sample():
    book = {
        'title' : 'test_title',
        'authors' : ['test_author1', 'test_author2'],
        'publishedDate' : '2010-01-01',
        'industryIdentifiers' : [
            {'type' : 'ISBN_13', 'identifier' : '1234567890123'},
        ],
        'pagesCount' : '300',
        'imageLinks' : {
            'thumbnail' : 'https://samplelink.com',
            'smallThumbnail' : 'https://samplelink2.com'
             },
        'language' : 'pl',
    }
    return book

@pytest.fixture
def book():
    book = {
        'volumeInfo' : {
            'title' : 'test_title',
            'authors' : ['test_author1', 'test_author2'],
            'publishedDate' : '2010-01-01',
            'industryIdentifiers' : [
                {'type' : 'ISBN_13', 'identifier' : '1234567890123'},
            ],
            'pagesCount' : '300',
            'imageLinks' : {
                'thumbnail' : 'https://samplelink.com',
                'smallThumbnail' : 'https://samplelink2.com'
                 },
            'language' : 'pl',
            }
    }
    return book

@pytest.fixture
def book_model_data_list():
    book_model_data = {
        'title' : 'test_title',
        'author' : 'test_author1',
        'published_date' : '2010-01-01',
        'isbn_13' : '1234567890123',
        'pages' : '300',
        'cover_link' : 'https://samplelink.com',
        'publication_language' : 'pl',
    }
    return [book_model_data]

@pytest.fixture
def form_data():
    data = {
        'intitle' : 'title',
        'inauthor' : 'author',
        'inpublisher' : 'publisher',
        'subject' : 'subject',
        'isbn' : '1234567890123',
        'lcnn' : '123',
        'oclc' : '456'
    }
    return data

@pytest.fixture
def form_empty_data():
    data = {
        'intitle' : '',
        'inauthor' : '',
        'inpublisher' : '',
        'subject' : '',
        'isbn' : '',
        'lcnn' : '',
        'oclc' : ''
    }
    return data
