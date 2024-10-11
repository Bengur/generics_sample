from django.urls import path
from library.views.book_views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path(
        "books/<int:pk>/", BookRetrieveUpdateDestroyView.as_view(), name="book-detail"
    ),
]
