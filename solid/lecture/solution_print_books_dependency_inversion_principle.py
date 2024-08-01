from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:3]


class FBFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:20]


class Printer:
    def get_book(self, book: Book, formmater: BaseFormatter):
        formatted_book = formmater.format(book)
        return formatted_book


book = Book('Some really really really long book')
p = Printer()
print(p.get_book(book, FBFormatter()))
