from rest_framework import generics
from .serializers import BookSerializer, TagSerializer
from rest_framework.authentication import TokenAuthentication
from .models import Book, Tag

class ListCreateBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)

class RetrieveUpdateDestroyBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
