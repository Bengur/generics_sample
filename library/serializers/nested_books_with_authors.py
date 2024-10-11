from library.models import Book, Author
from rest_framework import serializers


class NestedAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "birth_date")


class BookWithAuthorNestedSerializer(serializers.ModelSerializer):
    author = NestedAuthorSerializer()

    class Meta:
        model = Book
        fields = ("id", "title", "publication_date", "author")

    def create(self, validated_data):
        author_data = validated_data.pop("author")
        author, _ = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop("author", None)
        if author_data:
            Author.objects.filter(id=instance.author.id).update(**author_data)
        return super().update(instance, validated_data)
