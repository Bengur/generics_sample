from base.views.list_create_generics import BaseListCreateGenericAPIView
from config.swagger import add_swagger_tag
from library.models import Author
from library.serializers.nested_authors_with_books import (
    AuthorWithBooksNestedSerializer,
)
from rest_framework import generics

swagger_tags = ["nested authors with books"]


@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "post"])
class AuthorListCreateView(BaseListCreateGenericAPIView):
    queryset = Author.objects.all().prefetch_related("books")
    serializer_class = AuthorWithBooksNestedSerializer


@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "put", "patch", "delete"])
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all().prefetch_related("books")
    serializer_class = AuthorWithBooksNestedSerializer
