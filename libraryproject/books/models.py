from datetime import date

from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator

from django_date_extensions import fields

from .languages import languages


class Book(models.Model):
    title = models.CharField(max_length=256)
    published_date = fields.ApproximateDateField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(
                limit_value=date.today)])
    isbn_13 = models.CharField(max_length=13, unique=True, null=True,
                               blank=True, validators=[MinLengthValidator(13)])
    pages = models.PositiveSmallIntegerField(null=True, blank=True)
    cover_link = models.URLField(max_length=400, null=True, blank=True)
    publication_language = models.CharField(max_length=3, choices=languages,
                                            null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'published_date', 'isbn_13',
                        'pages', 'publication_language'],
                name='unique_joining',
            )
        ]


class Author(models.Model):
    name = models.CharField(max_length=256)
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
