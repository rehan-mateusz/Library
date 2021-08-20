from libraryproject import settings

def prepare_url(form):
    url = 'https://www.googleapis.com/books/v1/volumes?q='
    for key, value in form.cleaned_data.items():
        if value:
            url = url + key + ':' + value + '+'
    url = url[:-1] + '&key=' + settings.GOOGLE_API_KEY
    return url
