from config.swagger import add_swagger_tag
from library.models import Book
from library.serializers.nested_books_with_authors import BookWithAuthorNestedSerializer
from rest_framework import generics

swagger_tags = ["nested books with authors"]


@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "post"])
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().select_related("author")
    serializer_class = BookWithAuthorNestedSerializer


@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "put", "patch", "delete"])
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().select_related("author")
    serializer_class = BookWithAuthorNestedSerializer
