def get_books_model_data(books_list):

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
        else:
            return None

    def get_author(book):
        if 'authors' in book:
            return book['authors'][0]
        return None

    def get_pub_date(book):
        if 'publishedDate' in book:
            date = book['publishedDate']
            if len(date) not in (4, 6, 7, 8, 10):
                return None
            elif len(date) == 4:
                return date+'-0-0'
            elif date.count('-') == 2:
                return date
            elif date.count('-') == 1:
                return date + '-0'
        else:
            return None

    books_model_data=[]
    for book in books_list:
        book = book['volumeInfo']
        book_model_data = {
            'title' : get_value(book, 'title'),
            'author' : get_author(book),
            'published_date' : get_pub_date(book),
            'isbn_13' : get_isbn(book),
            'pages' : get_value(book, 'pagesCount'),
            'cover_link' : get_image_url(book),
            'publication_language' : get_value(book, 'language'),
        }
        books_model_data.append(book_model_data)
    return books_model_data
