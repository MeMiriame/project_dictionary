from book import Book
from author import Author

def test_book_title():
    author = Author(1, "George", "Orwell", "Denkmark")
    book = Book(1, "1984", author, 1949, "crimi", 4.5, False)
    assert book.name == "1984"

def test_book_invalid_review_type():
    author = Author(1, "George", "Orwell", "Denkmark")
    try:
        Book(1, "1984", author, 1949, "crimi", "vysoke", False)
        assert False, "TypeError not raised"
    except TypeError as e:
        assert str(e) == "Review must be a float"
