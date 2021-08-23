from django.urls import path

from . import views

app_name = 'books_rest'

urlpatterns = [
    path('books_rest/books_list/', views.BooksListAPIView.as_view()),
]
