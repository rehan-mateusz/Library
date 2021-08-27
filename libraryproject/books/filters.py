import django_filters

from . import models
from .languages import languages


class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Author:',
        field_name='author__name',)
    publication_language = django_filters.ChoiceFilter(choices=languages)
    published_after = django_filters.DateFilter(
        lookup_expr='gt',
        label='Published after:',
        field_name='published_date')
    published_before = django_filters.DateFilter(
        lookup_expr='lt',
        label='Published before:',
        field_name='published_date')

    class Meta:
        model = models.Book
        fields = {
            'title': ['icontains'],
        }
