import random

from django.core.management.base import BaseCommand
from faker import Faker
from library.models import Book, Author


class Command(BaseCommand):
    help = "Seeds the database with 100 authors and 2-10 books for each"

    def handle(self, *args, **kwargs):
        fake = Faker()
        self.stdout.write(self.style.SUCCESS("Starting data seeding..."))

        # Clear existing data
        Book.objects.all().delete()
        Author.objects.all().delete()

        # Seed 100 authors
        for _ in range(100):
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth_date = fake.date_of_birth(minimum_age=20, maximum_age=90)

            author = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
            )

            # Seed 2-10 books for each author
            num_books = random.randint(2, 10)
            for _ in range(num_books):
                title = fake.sentence(nb_words=5)
                publication_date = fake.date_between(
                    start_date="-50y", end_date="today"
                )

                Book.objects.create(
                    title=title,
                    publication_date=publication_date,
                    author=author,
                )

        self.stdout.write(self.style.SUCCESS("Data seeding completed successfully."))
