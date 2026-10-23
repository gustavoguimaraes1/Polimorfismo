from datetime import datetime
from functools import singledispatchmethod


class Author:

    def __init__(self, name: str):
        self.set_name(name)

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        if name == "":
            raise ValueError("O nome não pode ser vazio.")

        self.name = name


class Book:

    def __init__(self, title: str, author: Author, isbn: int, year: int):
        self.set_title(title)
        self.author = author
        self.set_isbn(isbn)
        self.set_year(year)

    def get_title(self):
        return self.title

    def set_title(self, title: str):
        if title == "":
            raise ValueError("O título não pode ser vazio.")

        self.title = title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn: int):
        if len(str(isbn)) != 13:
            raise ValueError("O ISBN deve possuir exatamente 13 dígitos.")

        self.isbn = isbn

    def get_year(self):
        return self.year

    def set_year(self, year: int):
        current_year = datetime.now().year

        if year < 0 or year > current_year:
            raise ValueError("Ano inválido.")

        self.year = year


class Library:

    def __init__(self, books: list[Book]):
        self.books = books

    @singledispatchmethod
    def search(self, query):
        raise TypeError("Critério não suportado")

    @search.register
    def _(self, query: str) -> list[Book]:
        result = []

        for book in self.books:
            if query.lower() in book.get_title().lower():
                result.append(book)

        return result

    @search.register
    def _(self, query: Author) -> list[Book]:
        result = []

        for book in self.books:
            if book.author is query:
                result.append(book)

        return result

    @search.register
    def _(self, query: int) -> list[Book]:
        result = []

        for book in self.books:
            if book.get_isbn() == query:
                result.append(book)

        return result

    @search.register
    def _(self, query: range) -> list[Book]:
        result = []

        for book in self.books:
            if book.get_year() in query:
                result.append(book)

        return result