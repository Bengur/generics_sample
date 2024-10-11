from django.urls import path
from library.views import nested_books_with_authors as nested


urlpatterns = [
    path("books/", nested.BookListCreateView.as_view(), name="book-list-create"),
    path(
        "books/<int:pk>/",
        nested.BookRetrieveUpdateDestroyView.as_view(),
        name="book-detail",
    ),
]
