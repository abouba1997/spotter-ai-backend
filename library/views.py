from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from auth.authentication import JWTAuthentication
from .models import Author, Genre, Book, FavoriteBook
from .serializers import GenreSerializer, BookSerializer, AuthorSerializer, FavoriteBookSerializer
from django.db.models import Q
from .recommendations import get_recommendations


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'authors__name']
    filterset_fields = ['language', 'publisher']


class FavoriteBookViewSet(viewsets.ModelViewSet):
    queryset = FavoriteBook.objects.all()
    serializer_class = FavoriteBookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return FavoriteBook.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def recommendations(self, request):
        user_favorites = self.get_queryset().values_list('book', flat=True)
        recommended_books = get_recommendations(user_favorites)
        serializer = BookSerializer(recommended_books, many=True)
        return Response(serializer.data)
