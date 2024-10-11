from django.urls import path
from library.views.nested_authors_with_books import (
    AuthorRetrieveUpdateDestroyView,
    AuthorListCreateView,
)

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view(), name="author-list-create"),
    path(
        "authors/<int:pk>/",
        AuthorRetrieveUpdateDestroyView.as_view(),
        name="author-detail",
    ),
]
