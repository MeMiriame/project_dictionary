from book import Book

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
    user11, user12, user13, user14, user15]




