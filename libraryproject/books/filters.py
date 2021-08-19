import django_filters

from . import models
from .languages import languages

class BookFilter(django_filters.FilterSet):
    publication_language = django_filters.ChoiceFilter(choices=languages)

    class Meta:
        model = models.Book
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
            'published_date': ['gt', 'lt'],
        }
