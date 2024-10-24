from django.db.models import Q
from django.db.models import Count
from .models import Genre, Book, FavoriteBook
from .serializers import BookSerializer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .ml_recommendations import recommendation_system


def get_recommendations(user_favorites, max_recommendations=5):
    recommended_books = recommendation_system.get_recommendations(
        user_favorites, max_recommendations)

    return recommended_books
