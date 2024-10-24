from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, BookViewSet, AuthorViewSet, FavoriteBookViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'favorites', FavoriteBookViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('auth.urls')),
]
