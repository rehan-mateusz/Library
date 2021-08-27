import pytest

from books import models

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
            'pageCount' : '300',
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
        'published_date' : '2010-01-01',
        'isbn_13' : '1234567890123',
        'pages' : '300',
        'cover_link' : 'https://samplelink.com',
        'publication_language' : 'pl',
    }
    book_model_data_list = {
        'book_model_data' : book_model_data,
        'authors' : ['test_author1', 'test_author2']
    }
    return [book_model_data_list]

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

@pytest.fixture
def book_form():

    class Form:
        def __init__(self):
            self.cleaned_data = {
                'title' : 'test_title',
                'published_date' : '2010-01-01',
                'isbn_13' : '1234567890123',
                'pages' : '300',
                'cover_link' : 'https://samplelink.com',
                'publication_language' : 'pl',
            }
    form = Form()
    return form

@pytest.fixture
def author_formset():

    class Form:
        def __init__(self, cleaned_data):
            self.cleaned_data = cleaned_data
            self.instance = models.Author(name=self.cleaned_data['name'])
    data1 = {
        'name' : 'test_author1',
        'book' : '',
        'DELETE' : 'FALSE'
    }
    data2 = {
        'name' : 'test_author2',
        'book' : '',
        'DELETE' : 'FALSE'
    }
    form = Form(data1)
    form2 = Form(data2)
    return (form, form2)
