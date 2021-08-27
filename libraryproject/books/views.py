import requests
import json

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django_filters.views import BaseFilterView

from . import models
from . import forms
from . import filters
from .data_processing import get_books_model_data
from .data_processing import save_books
from .data_processing import save_form_and_formset
from .prepare_url import prepare_url


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
                raise Http404(_("No %(verbose_name)s found matching the query") %
                              {'verbose_name': queryset.model._meta.verbose_name})
            return obj
        else:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.form_class)
        formset = forms.AuthorsFormSet(instance = self.object)
        return self.render_to_response(self.get_context_data(form=form,
                                                             formset=formset))

    def get_success_url(self):
        return reverse_lazy('books:books_list')

    def form_valid(self, form, formset):
        if self.object is not None:
            form.id = self.object.id
        self.object = save_form_and_formset(form, formset)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form,
                                                            formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = forms.AuthorsFormSet(self.request.POST,
                                       instance = self.object)

        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)


class GoogleBooksView(FormView):
    template_name = 'books/google_books_search.html'
    model = models.Book
    form_class = forms.GoogleForm

    def form_valid(self, form):
        url = prepare_url(form)
        client = requests.session()
        response = client.get(url)

        if response.json()['totalItems'] == 0:
            return HttpResponseRedirect(self.get_success_url())

        books_list = response.json()['items']
        books_model_data_list = get_books_model_data(books_list)
        save_books(books_model_data_list)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('books:books_list')
