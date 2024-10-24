from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="users_profile", blank=True, null=True)
    username = None

    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_users', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Author(models.Model):
    name = models.CharField(max_length=200)
    ratings_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    text_reviews_count = models.IntegerField(default=0)
    works_count = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, blank=True)
    image_url = models.URLField(blank=True)
    about = models.TextField(blank=True)
    fans_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    language = models.CharField(max_length=3)
    average_rating = models.FloatField(default=0.0)
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=200)
    num_pages = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title


class FavoriteBook(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def save(self, *args, **kwargs):
        if FavoriteBook.objects.filter(user=self.user).count() >= 20:
            raise ValidationError(
                "You can't have more than 20 favorite books.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.book}"
