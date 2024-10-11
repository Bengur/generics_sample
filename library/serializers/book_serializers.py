from library.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "publication_date", "author")
        read_only_fields = ("id",)
