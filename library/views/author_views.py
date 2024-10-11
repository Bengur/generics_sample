from base.views.list_create_generics import BaseListCreateGenericAPIView
from config.swagger import add_swagger_tag
from library.models import Author
from library.serializers.author_serializers import AuthorSerializer
from rest_framework import generics

swagger_tags = ["Authors"]


@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "post"])
class AuthorListCreateView(BaseListCreateGenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ["birth_date"]
    search_fields = ["first_name", "last_name", "user__username"]
    ordering_fields = ["first_name", "last_name", "birth_date"]
    ordering = ["last_name"]


@add_swagger_tag(swagger_tags=swagger_tags, methods=["get", "put", "patch", "delete"])
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
