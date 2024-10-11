from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters


class BaseListCreateGenericAPIView(generics.ListCreateAPIView):
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
