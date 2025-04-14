class Author:
    def __init__(self, id: int, first_name: str, last_name: str, country: str) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        if not isinstance(country, str):
            raise TypeError("Country must be a string")
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.country = country

class Book:
    def __init__(self, id: int, name: str, author: Author, year_publication: int, category: str, review: float,
                 borrow: bool) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        if not isinstance(year_publication, int):
            raise TypeError("Year publication must be an integer")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if not isinstance(review, float):
            raise TypeError("Review must be a float")


        self.id = id
        self.name = name
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

class User:
    def __init__(self, id: int, name: str, email: str, password: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.borrowed_books = []

    def borrow_book(self, book:Book):
        if not book.borrow:
            book.borrow = True
            self.borrowed_books.append(book)
            print(f"Book {self.name} borrowed")

    def return_book(self, book:Book):
            if book in self.borrowed_books:
                book.borrow = False
                self.borrowed_books.remove(book)
                print(f"{self.name} returned book: {book.name}")
            else:
                print(f"{self.name} has not borrowed: {book.name}.")

user1 = User(1, "Jana Novakova", "jana.novakova@email.cz", "heslo123")
user2 = User(2, "Petr Maly", "petr.maly@email.cz", "tajne456")
user3 = User(3, "Eva Velka", "eva.velka@email.cz", "mojeheslo789")
user4 = User(4, "Tomas Horak", "tomas.horak@email.cz", "abc123")
user5 = User(5, "Lucie Dvorakova", "lucie.d@email.cz", "lucinka456")
user6 = User(6, "Martin Kral", "martin.kral@email.cz", "kral2024")
user7 = User(7, "Barbora Kucerova", "bara.kucerova@email.cz", "kniha123")
user8 = User(8, "Ondrej Nemec", "ondrej.n@email.cz", "tajneheslo")
user9 = User(9, "Veronika Vesela", "verca.vesela@email.cz", "verca2024")
user10 = User(10, "Michal Urban", "michal.urban@email.cz", "urban123")
user11 = User(11, "Alena Cerna", "alena.cerna@email.cz", "cernalena")
user12 = User(12, "Filip Prochazka", "filip.prochazka@email.cz", "filip123")
user13 = User(13, "Helena Machova", "helena.m@email.cz", "machova2023")
user14 = User(14, "David Novotny", "david.novotny@email.cz", "novotnyheslo")
user15 = User(15, "Klara Ruzickova", "klara.ruzickova@email.cz", "ruzicka789")

users = [
    user1, user2, user3, user4, user5,
    user6, user7, user8, user9, user10,
    user11, user12, user13, user14, user15
]




