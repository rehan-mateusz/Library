from rest_framework import generics
from django_filters import rest_framework as filters

from . import filters
from . import serializers

from books import models

class BooksListAPIView(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BooksSerializer
    filterset_class = filters.BookFilter
