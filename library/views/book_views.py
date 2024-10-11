from base.views.list_create_generics import BaseListCreateGenericAPIView
from config.swagger import add_swagger_tag
from library.models import Book
from library.serializers.book_serializers import BookSerializer
from rest_framework import generics

swagger_tags = ["Books"]


# заметка
# все эти методы дженериков можно удобно соверрайдить,  они очень гибкие
# есть get_queryset вместо queryset =,
# есть get_object, get_serializer, методы для получения фильтров и все такое
@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "post"])
class BookListCreateView(BaseListCreateGenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = [
        "publication_date",
        "author",
    ]  # все что нужно, для фильтрации,
    # достаточно добавить в квери параметрах ?author=1&publication_date=1989-09-02 и отфлильтруются именно эти книги
    search_fields = ["title", "author__first_name"]
    ordering_fields = [
        "title",
        "publication_date",
    ]  # заполняем поля, которые нужны для сортировки,
    # в запросе поля передаются согласно своему названию или со знаком - и названию (чтоб по убыванию сортировать)
    ordering = ["title"]

    # пример урла со всеми квери параметрами
    # http://127.0.0.1:8000/library/books/books/?author=1&ordering=-publication_date&publication_date=1989-09-02&search=Jane


@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "put", "patch", "delete"])
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
