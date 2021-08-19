import requests
import json

from django.shortcuts import render
from django.views.generic import  ListView
from django.views.generic import  UpdateView
from django.views.generic import  FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django_filters.views import BaseFilterView

from . import models
from . import forms
from . import filters
from .data_processing import get_books_model_data
from libraryproject import settings

class BookListView(BaseFilterView, ListView):

    model = models.Book
    filterset_class = filters.BookFilter

class BookUpdateOrCreateView(UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'books/book_update.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
            queryset = queryset.filter(pk=pk)
            try:
                obj = queryset.get()
            except queryset.model.DoesNotExist:
                raise Http404(_("No %(verbose_name)s found matching the query")%
                      {'verbose_name': queryset.model._meta.verbose_name})
            return obj
        else:
            return None

    def get_success_url(self):
        return reverse_lazy('books:books_list')

class GoogleBooksView(FormView):
    template_name = 'books/google_books_search.html'
    model = models.Book
    form_class = forms.GoogleForm

    def form_valid(self, form):
        def prepare_url(form):
            url = 'https://www.googleapis.com/books/v1/volumes?q='
            for key, value in form.cleaned_data.items():
                if value:
                    url = url + key + ':' + value + '+'
            url = url[:-1] + '&key=' + settings.GOOGLE_API_KEY
            return url
        url = prepare_url(form)
        client = requests.session()
        response = client.get(url)

        books_list = response.json()['items']
        books_model_data_list = get_books_model_data(response.json()['items'])
        for book in books_model_data_list:
            if not models.Book.objects.filter(isbn_13=book['isbn_13']).count():
                try:
                    new_book = models.Book(**book)
                    new_book.save()
                except:
                    pass

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('books:books_list')
