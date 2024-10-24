from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils import timezone
from library.models import User, Genre, Author, Book, FavoriteBook


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        users_data = [
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "email": "alice@example.com",
                "password": "password123"
            },
            {
                "first_name": "Bob",
                "last_name": "Johnson",
                "email": "bob@example.com",
                "password": "password123"
            },
            {
                "first_name": "Charlie",
                "last_name": "Williams",
                "email": "charlie@example.com",
                "password": "password123"
            }
        ]

        for user_data in users_data:
            user, created = User.objects.get_or_create(
                email=user_data['email'])
            if created:
                user.first_name = user_data['first_name']
                user.last_name = user_data['last_name']
                user.set_password(user_data['password'])
                user.save()
                print(f"Seeded user: {user}")
            else:
                print(f"User already exists: {user}")

        authors_data = [
            {
                "name": "J.K. Rowling",
                "ratings_count": 1000000,
                "average_rating": 4.5,
                "text_reviews_count": 500000,
                "works_count": 7,
                "gender": "Female",
                "image_url": "https://example.com/jk_rowling.jpg",
                "about": "British author, best known for the Harry Potter series.",
                "fans_count": 2000000
            },
            {
                "name": "George R.R. Martin",
                "ratings_count": 500000,
                "average_rating": 4.7,
                "text_reviews_count": 250000,
                "works_count": 5,
                "gender": "Male",
                "image_url": "https://example.com/george_rr_martin.jpg",
                "about": "American novelist and short story writer, known for A Song of Ice and Fire.",
                "fans_count": 1500000
            },
            {
                "name": "Terry Pratchett",
                "ratings_count": 300000,
                "average_rating": 4.6,
                "text_reviews_count": 100000,
                "works_count": 41,
                "gender": "Male",
                "image_url": "https://example.com/terry_pratchett.jpg",
                "about": "English author known for his Discworld series.",
                "fans_count": 1200000
            },
            {
                "name": "J.R.R. Tolkien",
                "ratings_count": 800000,
                "average_rating": 4.8,
                "text_reviews_count": 600000,
                "works_count": 4,
                "gender": "Male",
                "image_url": "https://example.com/jrr_tolkien.jpg",
                "about": "English writer and professor, known for The Hobbit and The Lord of the Rings.",
                "fans_count": 2500000
            },
            {
                "name": "Isaac Asimov",
                "ratings_count": 450000,
                "average_rating": 4.5,
                "text_reviews_count": 200000,
                "works_count": 14,
                "gender": "Male",
                "image_url": "https://example.com/isaac_asimov.jpg",
                "about": "American author and professor of biochemistry, known for his works in science fiction.",
                "fans_count": 900000
            },
            {
                "name": "Agatha Christie",
                "ratings_count": 900000,
                "average_rating": 4.3,
                "text_reviews_count": 500000,
                "works_count": 85,
                "gender": "Female",
                "image_url": "https://example.com/agatha_christie.jpg",
                "about": "British writer known for her detective novels.",
                "fans_count": 3000000
            },
            {
                "name": "Paulo Coelho",
                "ratings_count": 2000000,
                "average_rating": 4.3,
                "text_reviews_count": 150000,
                "works_count": 30,
                "gender": "Male",
                "image_url": "https://example.com/paulo_coelho.jpg",
                "about": "Brazilian author, best known for The Alchemist.",
                "fans_count": 1800000
            },
            {
                "name": "Markus Zusak",
                "ratings_count": 1000000,
                "average_rating": 4.4,
                "text_reviews_count": 50000,
                "works_count": 6,
                "gender": "Male",
                "image_url": "https://example.com/markus_zusak.jpg",
                "about": "Australian author, known for The Book Thief.",
                "fans_count": 800000
            },
            {
                "name": "Madeline Miller",
                "ratings_count": 350000,
                "average_rating": 4.4,
                "text_reviews_count": 25000,
                "works_count": 2,
                "gender": "Female",
                "image_url": "https://example.com/madeline_miller.jpg",
                "about": "American author, known for Circe.",
                "fans_count": 600000
            },
            {

                "name": "John Green",
                "ratings_count": 300000,
                "average_rating": 4.5,
                "text_reviews_count": 15000,
                "works_count": 7,
                "gender": "Male",
                "image_url": "https://example.com/john_green.jpg",
                "about": "American author, known for The Fault in Our Stars.",
                "fans_count": 1200000
            }
        ]

        for author_data in authors_data:
            author, created = Author.objects.get_or_create(
                name=author_data['name'],
                defaults={
                    "ratings_count": author_data.get('ratings_count'),
                    "average_rating": author_data.get('average_rating'),
                    "text_reviews_count": author_data.get('text_reviews_count'),
                    "gender": author_data.get('gender'),
                    "image_url": author_data.get('image_url'),
                    "about": author_data.get('about'),
                    "fans_count": author_data.get('fans_count'),
                }
            )

            if created:
                print(f"Seeded new author: {author}")
            else:
                print(f"Author already exists: {author}")

        genres_data = [
            {"name": "Fantasy"},
            {"name": "Science Fiction"},
            {"name": "Mystery"},
            {"name": "Horror"},
            {"name": "Romance"},
            {"name": "Thriller"},
            {"name": "Dystopian"},
            {"name": "Adventure"},
            {"name": "Historical Fiction"},
            {"name": "Poetry"},
            {"name": "Self-Help"},
            {"name": "Cooking"},
            {"name": "Travel"},
            {"name": "Children's Books"},
            {"name": "Memoir"},
            {"name": "Biography"},
            {"name": "Autobiography"},
            {"name": "Art"},
            {"name": "Comics"},
            {"name": "Humor"},
            {"name": "History"},
            {"name": "Science"},
            {"name": "Philosophy"},
            {"name": "Magical Realism"},
            {"name": "Cyberpunk"},
            {"name": "Western"},
            {"name": "Graphic Novel"},
            {"name": "Young Adult"},
            {"name": "New Adult"},
            {"name": "Classic Literature"},
            {"name": "Literary Fiction"},
            {"name": "True Crime"},
            {"name": "Sports Fiction"},
            {"name": "Urban Fantasy"},
            {"name": "Chick Lit"},
            {"name": "Gothic Fiction"},
            {"name": "Satire"},
            {"name": "Anthology"},
            {"name": "Narrative Non-Fiction"},
            {"name": "Environmental Fiction"},
            {"name": "Fable"},
            {"name": "Fairy Tale"},
            {"name": "Steampunk"},
            {"name": "Alternate History"},
            {"name": "Psychological Thriller"},
            {"name": "Space Opera"},
            {"name": "Romantic Comedy"},
            {"name": "Family Saga"},
            {"name": "Coming-of-Age"},
            {"name": "Post-Apocalyptic"},
            {"name": "Surrealism"},
            {"name": "Flash Fiction"},
            {"name": "Experimental Fiction"},
            {"name": "Bizarro Fiction"},
            {"name": "Cozy Mystery"},
            {"name": "Military Fiction"},
            {"name": "Historical Romance"},
            {"name": "Dark Fantasy"},
            {"name": "Slice of Life"},
            {"name": "Inspirational Fiction"},
            {"name": "Techno-thriller"},
            {"name": "Romantic Suspense"},
            {"name": "Medical Thriller"},
            {"name": "Legal Thriller"},
            {"name": "Travel Memoir"},
            {"name": "Cultural Criticism"},
            {"name": "Social Commentary"},
            {"name": "Feminist Literature"},
            {"name": "LGBTQ+ Fiction"},
            {"name": "Mythology"},
            {"name": "Animal Fiction"},
            {"name": "Historical Mystery"},
            {"name": "Cozy Fantasy"},
            {"name": "Dramatic Fiction"},
            {"name": "Epic Fantasy"},
            {"name": "Noir Fiction"},
            {"name": "Whodunit"},
            {"name": "Romantic Fantasy"},
            {"name": "Cyber Noir"},
            {"name": "Space Western"},
            {"name": "Time Travel Fiction"},
            {"name": "Dystopian Romance"},
            {"name": "Futuristic Fiction"},
            {"name": "Magical Realism"},
            {"name": "Paranormal Romance"},
            {"name": "Superhero Fiction"},
            {"name": "Historical Adventure"},
            {"name": "Culinary Fiction"},
            {"name": "Art History"},
            {"name": "Philosophical Fiction"},
            {"name": "Rural Fiction"},
            {"name": "Urban Fiction"},
            {"name": "Intergalactic Fiction"},
            {"name": "Feminist Science Fiction"},
            {"name": "Postmodern Fiction"},
            {"name": "Transgressive Fiction"},
            {"name": "Crossover Fiction"},
            {"name": "Speculative Fiction"},
            {"name": "Young Adult Fantasy"},
            {"name": "Young Adult Science Fiction"},
            {"name": "Young Adult Romance"},
            {"name": "Young Adult Mystery"},
            {"name": "Young Adult Horror"},
            {"name": "Young Adult Dystopian"},
            {"name": "Young Adult Historical Fiction"},
            {"name": "Young Adult Contemporary Fiction"},
            {"name": "Young Adult Magical Realism"},
            {"name": "Young Adult Adventure"},
            {"name": "Young Adult Thriller"},
            {"name": "Young Adult Literary Fiction"},
            {"name": "Young Adult Graphic Novel"},
            {"name": "Young Adult Anthology"},
            {"name": "Young Adult Poetry"}
        ]

        for genre_data in genres_data:
            try:
                genre, created = Genre.objects.get_or_create(
                    name=genre_data['name']
                )
                if created:
                    print(f"Seeded new genre: {genre}")
                else:
                    print(f"Genre already exists: {genre}")
            except Genre.DoesNotExist:
                print(f"Genre with ID {genre_data['name']} does not exist")

        books_data = [
            {
                "title": "Harry Potter and the Sorcerer's Stone",
                "authors": [1],
                "genres": [1, 28],
                "isbn": "9780439554930",
                "language": "en",
                "average_rating": 4.8,
                "ratings_count": 5000000,
                "text_reviews_count": 1000000,
                "publication_date": "1997-09-01",
                "publisher": "Scholastic",
                "num_pages": 309,
                "description": "A young boy discovers he is a wizard and attends Hogwarts School of Witchcraft and Wizardry."
            },
            {
                "title": "A Game of Thrones",
                "authors": [2],
                "genres": [1, 7],
                "isbn": "9780553103540",
                "language": "en",
                "average_rating": 4.7,
                "ratings_count": 3000000,
                "text_reviews_count": 250000,
                "publication_date": "1996-08-06",
                "publisher": "Bantam Books",
                "num_pages": 694,
                "description": "The first book in the A Song of Ice and Fire series, introducing the world of Westeros."
            },
            {
                "title": "Good Omens",
                "authors": [3],
                "genres": [20, 36],
                "isbn": "9780060853983",
                "language": "en",
                "average_rating": 4.5,
                "ratings_count": 800000,
                "text_reviews_count": 150000,
                "publication_date": "1990-05-01",
                "publisher": "Gollancz",
                "num_pages": 288,
                "description": "A comedic tale of an angel and a demon teaming up to stop the apocalypse."
            },
            {
                "title": "The Hobbit",
                "authors": [4],
                "genres": [1, 48],
                "isbn": "9780345339683",
                "language": "en",
                "average_rating": 4.8,
                "ratings_count": 2500000,
                "text_reviews_count": 500000,
                "publication_date": "1937-09-21",
                "publisher": "Houghton Mifflin",
                "num_pages": 310,
                "description": "A fantasy novel about the adventures of Bilbo Baggins."
            },
            {
                "title": "The Martian",
                "authors": [5],
                "genres": [2, 22],
                "isbn": "9780553418026",
                "language": "en",
                "average_rating": 4.7,
                "ratings_count": 3000000,
                "text_reviews_count": 200000,
                "publication_date": "2014-02-11",
                "publisher": "Crown Publishing Group",
                "num_pages": 369,
                "description": "A science fiction novel about an astronaut stranded on Mars."
            },
            {
                "title": "Murder on the Orient Express",
                "authors": [6],
                "genres": [3, 61],
                "isbn": "9780062073494",
                "language": "en",
                "average_rating": 4.5,
                "ratings_count": 2000000,
                "text_reviews_count": 100000,
                "publication_date": "1934-01-01",
                "publisher": "Collins Crime Club",
                "num_pages": 256,
                "description": "A detective novel featuring Hercule Poirot investigating a murder on a train."
            },
            {
                "title": "The Alchemist",
                "authors": [7],
                "genres": [14, 49],
                "isbn": "9780062315007",
                "language": "en",
                "average_rating": 4.3,
                "ratings_count": 2000000,
                "text_reviews_count": 150000,
                "publication_date": "1988-05-01",
                "publisher": "HarperCollins",
                "num_pages": 208,
                "description": "A novel about following one's dreams and personal legend."
            },
            {
                "title": "Circe",
                "authors": [9],
                "genres": [1, 65],
                "isbn": "9780316388645",
                "language": "en",
                "average_rating": 4.4,
                "ratings_count": 350000,
                "text_reviews_count": 25000,
                "publication_date": "2018-04-10",
                "publisher": "Little, Brown and Company",
                "num_pages": 400,
                "description": "A retelling of the myth of Circe, the daughter of Helios, who discovers her power."
            },
            {
                "title": "The Fault in Our Stars",
                "authors": [10],
                "genres": [5, 68],
                "isbn": "9780525478812",
                "language": "en",
                "average_rating": 4.2,
                "ratings_count": 2500000,
                "text_reviews_count": 300000,
                "publication_date": "2012-01-10",
                "publisher": "Dutton Books",
                "num_pages": 313,
                "description": "A poignant tale of two teenage cancer patients who fall in love."
            },
            {
                "title": "A Clash of Kings",
                "authors": [2],
                "genres": [1, 7],
                "isbn": "9780553108579",
                "language": "en",
                "average_rating": 4.6,
                "ratings_count": 1500000,
                "text_reviews_count": 100000,
                "publication_date": "1998-11-16",
                "publisher": "Bantam Books",
                "num_pages": 768,
                "description": "The second book in the A Song of Ice and Fire series, continuing the epic story."
            },
            {
                "title": "Discworld: The Color of Magic",
                "authors": [3],
                "genres": [1, 36],
                "isbn": "9780552148041",
                "language": "en",
                "average_rating": 4.4,
                "ratings_count": 800000,
                "text_reviews_count": 100000,
                "publication_date": "1983-11-24",
                "publisher": "Corgi",
                "num_pages": 400,
                "description": "The first book in the Discworld series, introducing the flat world supported by four elephants."
            },
            {
                "title": "The Name of the Wind",
                "authors": [1, 4],
                "genres": [1, 58],
                "isbn": "9780756404741",
                "language": "en",
                "average_rating": 4.5,
                "ratings_count": 1500000,
                "text_reviews_count": 70000,
                "publication_date": "2007-03-27",
                "publisher": "DAW Books",
                "num_pages": 662,
                "description": "The story of Kvothe, a magically gifted young man, as he recounts his life's journey."
            },
            {
                "title": "The Handmaid's Tale",
                "authors": [1],
                "genres": [7, 66],
                "isbn": "9780385490818",
                "language": "en",
                "average_rating": 4.0,
                "ratings_count": 1000000,
                "text_reviews_count": 200000,
                "publication_date": "1985-04-17",
                "publisher": "McClelland & Stewart",
                "num_pages": 311,
                "description": "A dystopian novel set in a totalitarian society that treats women as property."
            },
            {
                "title": "Neverwhere",
                "authors": [1],
                "genres": [1, 33],
                "isbn": "9780755322800",
                "language": "en",
                "average_rating": 4.0,
                "ratings_count": 500000,
                "text_reviews_count": 80000,
                "publication_date": "1996-06-20",
                "publisher": "Headline Review",
                "num_pages": 368,
                "description": "A dark urban fantasy about a man who discovers a hidden world beneath London."
            },
            {
                "title": "The Night Circus",
                "authors": [1],
                "genres": [1, 24],
                "isbn": "9780385534635",
                "language": "en",
                "average_rating": 4.2,
                "ratings_count": 400000,
                "text_reviews_count": 50000,
                "publication_date": "2011-09-13",
                "publisher": "Doubleday",
                "num_pages": 512,
                "description": "A fantasy novel about a magical competition between two young illusionists."
            },
            {
                "title": "Fahrenheit 451",
                "authors": [1],
                "genres": [7, 29],
                "isbn": "9781451673319",
                "language": "en",
                "average_rating": 4.0,
                "ratings_count": 500000,
                "text_reviews_count": 100000,
                "publication_date": "1953-10-19",
                "publisher": "Simon & Schuster",
                "num_pages": 158,
                "description": "A dystopian novel about a future where books are banned and 'firemen' burn them."
            },
            {
                "title": "The Girl on the Train",
                "authors": [1],
                "genres": [6, 43],
                "isbn": "9781594634024",
                "language": "en",
                "average_rating": 4.1,
                "ratings_count": 1000000,
                "text_reviews_count": 150000,
                "publication_date": "2015-01-13",
                "publisher": "Riverhead Books",
                "num_pages": 336,
                "description": "A psychological thriller about a woman who becomes entangled in a missing person investigation."
            },
            {
                "title": "The Road",
                "authors": [1],
                "genres": [48, 50],
                "isbn": "9780307387899",
                "language": "en",
                "average_rating": 4.2,
                "ratings_count": 800000,
                "text_reviews_count": 100000,
                "publication_date": "2006-09-26",
                "publisher": "Knopf",
                "num_pages": 287,
                "description": "A post-apocalyptic novel following a father and son as they journey through a devastated America."
            },
            {
                "title": "Educated",
                "authors": [1],
                "genres": [15, 14],
                "isbn": "9780399590504",
                "language": "en",
                "average_rating": 4.5,
                "ratings_count": 200000,
                "text_reviews_count": 50000,
                "publication_date": "2018-02-20",
                "publisher": "Random House",
                "num_pages": 334,
                "description": "A memoir about a woman who grows up in a strict and abusive household in rural Idaho but eventually escapes to learn about the wider world."
            },
            {
                "title": "The Silent Patient",
                "authors": [1],
                "genres": [6, 43],
                "isbn": "9781250301697",
                "language": "en",
                "average_rating": 4.2,
                "ratings_count": 400000,
                "text_reviews_count": 20000,
                "publication_date": "2019-02-05",
                "publisher": "Celadon Books",
                "num_pages": 336,
                "description": "A psychological thriller about a woman who shoots her husband and then stops speaking."
            },
            {
                "title": "Where the Crawdads Sing",
                "authors": [1],
                "genres": [2, 52],
                "isbn": "9780735219090",
                "language": "en",
                "average_rating": 4.4,
                "ratings_count": 1000000,
                "text_reviews_count": 250000,
                "publication_date": "2018-08-14",
                "publisher": "G.P. Putnam's Sons",
                "num_pages": 368,
                "description": "A coming-of-age story intertwined with a murder mystery set in the marshes of North Carolina."
            }
        ]

        for book_data in books_data:
            try:
                authors_list = [Author.objects.get(
                    id=author_id) for author_id in book_data.pop("authors")]
                genres_list = [Genre.objects.get(
                    id=genre_id) for genre_id in book_data.pop("genres")]
                book, created = Book.objects.get_or_create(
                    title=book_data['title'],
                    defaults={
                        "isbn": book_data.get('isbn'),
                        "language": book_data.get('language'),
                        "average_rating": book_data.get('average_rating'),
                        "ratings_count": book_data.get('ratings_count'),
                        "text_reviews_count": book_data.get('text_reviews_count'),
                        "publication_date": book_data.get('publication_date'),
                        "publisher": book_data.get('publisher'),
                        "num_pages": book_data.get('num_pages'),
                        "description": book_data.get('description'),
                    }
                )
                book.authors.set(authors_list)
                book.genres.set(genres_list)

                if created:
                    print(f"Seeded new book: {book}")
                else:
                    print(f"Book already exists: {book}")
            except Author.DoesNotExist:
                print(f"Author with ID {book_data['author']} does not exist")

        user_favorites_data = [
            {
                "user_id": 1,
                "email": "alice@example.com",
                "favorites": [
                    {"book_id": 1, "title": "Harry Potter and the Sorcerer's Stone"},
                    {"book_id": 4, "title": "The Hobbit"},
                    {"book_id": 7, "title": "The Alchemist"},
                    {"book_id": 12, "title": "The Name of the Wind"},
                    {"book_id": 16, "title": "The Night Circus"}
                ]
            },
            {
                "user_id": 2,
                "email": "bob@example.com",
                "favorites": [
                    {"book_id": 2, "title": "A Game of Thrones"},
                    {"book_id": 6, "title": "Murder on the Orient Express"},
                    {"book_id": 8, "title": "Circe"},
                    {"book_id": 14, "title": "The Handmaid's Tale"},
                    {"book_id": 18, "title": "The Girl on the Train"}
                ]
            },
            {
                "user_id": 3,
                "email": "charlie@example.com",
                "favorites": [
                    {"book_id": 3, "title": "Good Omens"},
                    {"book_id": 5, "title": "The Martian"},
                    {"book_id": 9, "title": "The Fault in Our Stars"},
                    {"book_id": 11, "title": "Discworld: The Color of Magic"},
                    {"book_id": 21, "title": "Where the Crawdads Sing"}
                ]
            }
        ]

        for user_data in user_favorites_data:
            user = User.objects.get(
                email=user_data['email']
            )

            if not user:
                self.stdout.write(self.style.WARNING(
                    f"User with username {user_data['username']} does not exist. Skipping."))
                continue

            for book_id in user_data['favorites']:
                try:
                    book = Book.objects.get(id=book_id["book_id"])
                    FavoriteBook.objects.get_or_create(
                        user=user,
                        book=book,
                        defaults={'added_at': timezone.now()}
                    )
                except Book.DoesNotExist:
                    self.stdout.write(self.style.WARNING(
                        f"Book with id {book_id} does not exist. Skipping."))
                except IntegrityError:
                    self.stdout.write(self.style.WARNING(
                        f"Favorite for user {user.username} and book {book_id} already exists. Skipping."))

        self.stdout.write(self.style.SUCCESS("Seeding complete"))
