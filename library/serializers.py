from rest_framework import serializers
from .models import Genre, Book, Author, FavoriteBook
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        constraints = [
            UniqueConstraint(fields=['name'], name='unique_name'),
        ]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class FavoriteBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = FavoriteBook
        fields = '__all__'
