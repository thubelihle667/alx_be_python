class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_checked_out(self):
        return self.__is_checked_out


class Library:
    def __init__(self):
        self._books = []  # ✅ Match the exact expected attribute name

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return f"You have checked out '{book.title}' by {book.author}."
        return "Book not available or already checked out."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return f"You have returned '{book.title}'."
        return "This book was not checked out."

    def list_available_books(self):
        Book.list_available_books(self._books)

