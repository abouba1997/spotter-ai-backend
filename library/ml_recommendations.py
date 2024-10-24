import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Book


class MLRecommendationSystem:
    def __init__(self):
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.book_features = None
        self.book_ids = None
        self.similarity_matrix = None

    def fit(self):
        books = Book.objects.all()
        self.book_ids = [book.id for book in books]

        # Create the content to be used for TF-IDF: combining title, language, description, genres and authors
        book_contents = [
            f"{book.title} {book.language} {book.description} {' '.join(genre.name for genre in book.genres.all())} {' '.join(author.name for author in book.authors.all())}"
            for book in books
        ]

        # Transform the book contents into TF-IDF features and calculate similarity matrix
        self.book_features = self.tfidf.fit_transform(book_contents)
        self.similarity_matrix = cosine_similarity(self.book_features)

    def get_recommendations(self, user_favorites, max_recommendations=5):
        # Fit the model if it hasn't been fitted yet
        if self.similarity_matrix is None:
            self.fit()

        # Convert user favorite book IDs into their corresponding indices in the similarity matrix
        favorite_indices = [self.book_ids.index(
            book_id) for book_id in user_favorites if book_id in self.book_ids]

        # If the user has no favorite books, return an empty list
        if not favorite_indices:
            return []

        # Compute the user profile by averaging the favorite books' feature vectors
        user_profile = np.mean(self.book_features[favorite_indices], axis=0)

        # Convert to numpy array to avoid matrix issues
        user_profile = np.asarray(user_profile)

        # Compute similarity scores between the user profile and all books
        similarity_scores = cosine_similarity(
            user_profile, self.book_features)[0]

        # Get book indices sorted by similarity score (highest first)
        recommended_indices = similarity_scores.argsort()[::-1]

        # Exclude already favorited books from recommendations
        recommended_indices = [
            idx for idx in recommended_indices if self.book_ids[idx] not in user_favorites]

        # Select top N recommendations based on max_recommendations
        recommended_book_ids = [self.book_ids[idx]
                                for idx in recommended_indices[:max_recommendations]]

        # Fetch and return the recommended books from the database
        return Book.objects.filter(id__in=recommended_book_ids)


recommendation_system = MLRecommendationSystem()
