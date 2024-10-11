from drf_writable_nested import WritableNestedModelSerializer
from library.models import Book, Author
from rest_framework import serializers


class NestedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "publication_date"]
        read_only_fields = ["id"]


class AuthorWithBooksNestedSerializer(WritableNestedModelSerializer):

    books = NestedBookSerializer(many=True)

    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "birth_date", "books"]
        read_only_fields = ["id"]
