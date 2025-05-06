from author import Author

class Book:
    def __init__(self, id: int, title: str, author: Author, year_publication: int, category: str, review: float,
                 borrow: bool) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if not isinstance(title, str):
            raise TypeError("Name must be a string")
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance")
        if not isinstance(year_publication, int):
            raise TypeError("Year publication must be an integer")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if not isinstance(review, float):
            raise TypeError("Review must be a float")


        self.id = id
        self.name = title
        self.author = author
        self.year_publication = year_publication
        self.category = category
        self.review = review
        self.borrow = borrow

    def borrow(self):
        if not self.borrow:
            self.borrow = True
            print(f"Kniha {self.name} borrowed")
        if self.borrow:
            self.borrow = False
            print(f"Kniha {self.name} is free")
            