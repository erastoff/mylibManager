# -*- coding: utf-8 -*-
import functools
import unittest

from main import Book, Library


def cases(cases):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args):
            for c in cases:
                new_args = args + (c if isinstance(c, tuple) else (c,))
                f(*new_args)

        return wrapper

    return decorator


class TestBooks(unittest.TestCase):
    def setUp(self):
        self.test_title = "test_title"
        self.test_author = "test_author"
        self.test_year = 2000
        self.test_status = "test_status"

        self.new_book = Book(
            title=self.test_title,
            author=self.test_author,
            year=self.test_year,
            status=self.test_status,
        )

    def test_create_book(self):
        self.assertEqual(self.new_book.title, self.test_title)
        self.assertEqual(self.new_book.author, self.test_author)
        self.assertEqual(self.new_book.year, self.test_year)
        self.assertEqual(self.new_book.status, self.test_status)

    @cases(
        [
            {
                "id": 1000,
                "title": "11.22.63",
                "author": "Stephen King",
                "year": 2011,
                "status": "в наличии",
            },
            {
                "id": 2000,
                "title": "Будущее",
                "author": "Дмитрий Глуховский",
                "year": 2010,
                "status": "в наличии",
            },
            {
                "id": 3000,
                "title": "Метро 2033",
                "author": "Дмитрий Глуховский",
                "year": 2010,
                "status": "в наличии",
            },
        ]
    )
    def test_create_books_from_dict(self, arguments):
        instances = Book.from_dict(arguments)

        self.assertEqual(instances.id, arguments["id"])
        self.assertEqual(instances.title, arguments["title"])
        self.assertEqual(instances.author, arguments["author"])
        self.assertEqual(instances.year, arguments["year"])
        self.assertEqual(instances.status, arguments["status"])

    def test_created_dict_from_instance(self):
        test_dict = self.new_book.to_dict()

        self.assertEqual(test_dict["id"], self.new_book.id)
        self.assertEqual(test_dict["title"], self.test_title)
        self.assertEqual(test_dict["author"], self.test_author)
        self.assertEqual(test_dict["year"], self.test_year)
        self.assertEqual(test_dict["status"], self.test_status)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.test_library = Library("test_library.json")

    def test_existent_library(self):
        self.assertTrue(isinstance(self.test_library, Library))
        self.assertEqual(len(self.test_library.books), 4)
        # params = (
        #     {
        #         "author": "Дмитрий Глуховский",
        #     },
        # )
        for book in self.test_library.books:
            pass

    def test_not_existent_library(self):
        pass


if __name__ == "__main__":
    unittest.main()
