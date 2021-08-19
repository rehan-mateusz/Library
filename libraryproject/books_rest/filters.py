from django_filters import rest_framework as filters

from books import models
from books.languages import languages

class BookFilter(filters.FilterSet):
    publication_language = filters.ChoiceFilter(choices=languages)
    published_after = filters.DateFilter(lookup_expr='gt',
        label='Published after:', field_name='published_date')
    published_before = filters.DateFilter(lookup_expr='lt',
        label='Published before:', field_name='published_date')

    class Meta:
        model = models.Book
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
        }
