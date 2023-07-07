from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from book.pagination import BookPagination


# Create your views here.
class BookListCreateView(generics.ListCreateAPIView):
    pagination_class = BookPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
