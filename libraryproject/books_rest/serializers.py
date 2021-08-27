from rest_framework import serializers

from books import models

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = ['name',]


class BooksSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True, source='author_set')
    class Meta:
        model = models.Book
        fields = '__all__'
