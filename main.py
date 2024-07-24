# -*- coding: utf-8 -*-
import json
import os


# Define the file name where the library data will be stored
LIBRARY_FILE = "library.json"


# Book class to represent each book in the library
class Book:
    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        book_id: int = None,
        status: str = "в наличии",
    ):
        self.id = book_id or self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @staticmethod
    def generate_id() -> int:
        # Generate a unique id based on the current timestamp and a random element
        import time

        return int(time.time() * 1000)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["title"], data["author"], data["year"], data["id"], data["status"]
        )


# Library class to manage the collection of books
class Library:
    def __init__(self, library_file: str = LIBRARY_FILE):
        self.library_file = library_file
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.library_file):
            with open(self.library_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]

    def save_books(self):
        with open(self.library_file, "w", encoding="utf-8") as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def add_book(self, title: str, author: str, year: int):
        book = Book(title.strip(), author.strip(), year)
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {book.id}.")

    def delete_book(self, book_id: int):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id: int) -> Book:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, title: str = None, author: str = None, year: int = None):
        results = [
            book
            for book in self.books
            if (title and title.lower() in book.title.lower())
            or (author and author.lower() in book.author.lower())
            or (year and year == book.year)
        ]

        if not title and not author and not year or not results:
            print("\nКниги не найдены!")
            return

        print(f"Найдено экземпляров: {len(results)}\n")
        self.display_books(results)

    def display_book(self, book_id: int):
        book = self.find_book_by_id(book_id)
        print(
            f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}"
        )

    def display_books(self, books=None):
        books = books or self.books
        for book in books:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}"
            )

    def update_book_status(self, book_id: int, status: str):
        book = self.find_book_by_id(book_id)

        if book:
            book.status = status
            self.save_books()
            print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")


def main():
    library = Library()

    while True:
        print("\nМеню библиотеки:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")
        match choice:

            case "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                while True:
                    try:
                        year = int(input("Введите год издания книги: "))
                    except ValueError:
                        print("Некорректные данные года издания.")
                        continue
                    break
                library.add_book(title, author, year)

            case "2":
                book_id = int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id)

            case "3":
                title = input(
                    "Введите название книги для поиска (нажмите Enter, чтобы пропустить): "
                )
                author = input(
                    "Введите автора книги для поиска (нажмите Enter, чтобы пропустить): "
                )
                year = input(
                    "Введите год издания книги для поиска (нажмите Enter, чтобы пропустить): "
                )
                year = int(year) if year else None
                library.search_books(title, author, year)

            case "4":
                library.display_books()

            case "5":
                book_id = int(input("Введите ID книги для изменения статуса: "))
                library.display_book(book_id)
                while True:
                    status = input(
                        "Введите новый статус книги ('в наличии' или 'выдана'): "
                    )
                    if (
                        status
                        and status.lower() not in ["выдана", "в наличии"]
                        or not status
                    ):
                        print(
                            "Статус введен неверно (допустимые значения поля 'в наличии' или 'выдана')."
                        )
                        continue
                    library.update_book_status(book_id, status.lower())
                    break

            case "6":
                print("Выход из программы.")
                break

            case _:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nВсего доброго!")
