from . import models


def get_books_model_data(books_list):
    books_model_data = []
    for book in books_list:
        book = book['volumeInfo']
        book_model_data = {
            'title': get_value(book, 'title'),
            'published_date': get_pub_date(book),
            'isbn_13': get_isbn(book),
            'pages': get_value(book, 'pageCount'),
            'cover_link': get_image_url(book),
            'publication_language': get_value(book, 'language'),
        }
        books_model_data.append({
            'book_model_data' : book_model_data,
            'authors' : get_authors(book)})
    return books_model_data


def get_isbn(book):
    if 'industryIdentifiers' in book:
        for identifier in book['industryIdentifiers']:
            if identifier['type'] == 'ISBN_13':
                return identifier['identifier']
    return None


def get_image_url(book):
    if 'imageLinks' in book:
        if 'thumbnail' in book['imageLinks']:
            return book['imageLinks']['thumbnail']
        elif 'smallThumbnail' in book['imageLinks']:
            return book['imageLinks']['smallThumbnail']
    return None


def get_value(book, key):
    if key in book:
        return book[key]
    return None


def get_authors(book):
    if 'authors' in book:
        return book['authors']
    return None


def get_pub_date(book):
    if 'publishedDate' in book:
        date = book['publishedDate']
        if len(date) not in (4, 6, 7, 8, 9, 10):
            return None
        elif len(date) == 4:
            return date + '-0-0'
        elif date.count('-') == 2:
            return date
        elif date.count('-') == 1:
            return date + '-0'
    return None


def save_books(books_model_data_list):
    for book_data in books_model_data_list:
        book = save_new_book_or_get_original(book_data['book_model_data'])
        if book_data['authors']:
            for author in book_data['authors']:
                is_duplicate = models.Author.objects.filter(
                    book=book,
                    name=author).count()
                if author and is_duplicate==0:
                    new_author = models.Author(book=book,
                                               name=author)
                    new_author.save()

def save_form_and_formset(form, formset):
    book = save_new_book_or_get_original(form.cleaned_data)
    for author in formset:
        if author.cleaned_data:
            if not author.instance.id:
                is_duplicate = models.Author.objects.filter(
                    book=book,
                    name=author.cleaned_data['name']).count()
                if not is_duplicate:
                    auth = models.Author(book = book,
                                         name = author.cleaned_data['name'])
                    auth.save()
            elif author.cleaned_data['DELETE']:
                auth = models.Author.objects.get(id=author.instance.id)
                auth.delete()
            else:
                auth = models.Author.objects.get(id=author.instance.id)
                auth.name = author.cleaned_data['name']
                auth.save()
    return book

def save_new_book_or_get_original(book_data):
    if book_data['isbn_13']:
        book_duplicates = models.Book.objects.filter(
            isbn_13=book_data['isbn_13'])
    else:
        book_duplicates = models.Book.objects.filter(
                                    **book_data)
    if book_duplicates.count() == 0:
        book = models.Book(**book_data)
        book.save()
    else:
        book = book_duplicates.first()
    return book
