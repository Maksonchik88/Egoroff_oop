class Library:
    def __init__(self, books: list) -> None:
        self.__books = books


    def __check_availability(self, book):
        return book in self.__books

    def search_book(self, book):
        return self.__check_availability(book)

    def return_book(self, book):
        self.__books.append(book)

    def _checkout_book(self, book):
        self.book = book
        if self.book in self.__books:
            self.__books.remove(self.book)
            return True

# Ниже код для проверки методов класса Library
library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')
