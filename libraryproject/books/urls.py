from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path(
        'books/',
        views.BookListView.as_view(),
        name='books_list'),
    path(
        'books/update_or_add/',
        views.BookUpdateOrCreateView.as_view(),
        name='book_add'),
    path(
        'books/update_or_add/<int:pk>',
        views.BookUpdateOrCreateView.as_view(),
        name='book_update'),
    path(
        'books/google_books_search/',
        views.GoogleBooksView.as_view(),
        name='google_search'),
]
